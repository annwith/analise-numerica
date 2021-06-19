import numpy as np
import matplotlib.pyplot as plt

# Interpolação por diferenças divididas de Newton
# Comparar com Lagrange: Tem que ser igual
# Porque Python? Flexibilidade no trabalho com listas
# Retirar e colocar pontos
def newton(pontos):
    x = pontos[:, 0]
    y = pontos[:, 1]
    n = len(x)

    # f[xi, xj] = (f(xi)-f(xj))/(xi-xj)

    # inicialização
    b = []
    for i in range(n-1):
        b.append((y[i]-y[i+1])/(x[i]-x[i+1]))

    l = []
    l.append(b)
    # print(l)

    # construção da arvore
    ind=0
    while len(l[ind])>1:
        b = []
        step = ind+2
        for i in range(len(l[ind])-1):
            b.append((l[ind][i]-l[ind][i+1])/(x[i]-x[i+step]))
        l.append(b)
        ind += 1

    # print(l)

    # construção de b
    b = []
    # b.append([y[0]])
    for i in range(len(l)):
        b.append([l[i][0]])

    # print(b)

    # construção de f
    termos = 1
    fx = []
    for i in range(n-1):
        f = []
        for j in range(termos):
            f.append([-x[j], 1])
        fx.append(f)
        termos += 1

    # print(fx)

    # Multiplica dois polinomios
    # A posição em p1 e p2 indica o grau e o valor o coeficiente: [-6, 1] = x-6
    def mul(p1, p2):
        grau_max = p1.shape[0]+p2.shape[0]-1
        p = np.zeros((grau_max)) # grau maximo do polinomio resultante
        for i in range(p1.shape[0]):
            for j in range(p2.shape[0]):
                grau = i+j # descobrir o grau
                p[grau] += p1[i]*p2[j] # multiplicar coeficientes
        return p

    # resolver a multiplicação de polinomios de fx
    p = []
    for i in range(n-1):
        p.append(np.asarray(fx[i][0]))

    for i in range(n-1):
        for j in range(1, len(fx[i])):
            p[i] = mul(p[i], np.asarray(fx[i][j]))

    # print(p)

    # multiplicar por b
    for i in range(n-1):
        p[i] *= b[i]

    # print(p)

    # somar tudo
    fx = []
    for i in range(n):
        fx.append(0)
        if i != 0:
            start = i-1
        else:
            start = 0
        for j in range(start, len(p)):
            fx[i] += p[j][i]
            print(p[j][i])
    # print(fx)

    # não esquecer do b0
    fx[0] += y[0]
    fx = np.asarray(fx)
    print(fx)

    return fx

def predicao(a, x):
    y = 0
    for j in range(a.shape[0]):
        y += a[j]*x**(j)
    return y

def mostrar_grafico(pontos, a):
    # Data for plotting
    pontos = np.asarray(pontos)
    x = pontos[:, 0]
    y = pontos[:, 1]

    # Data for plotting
    h_grafico = abs(x[0]-x[-1])/100
    xl = np.arange(x[0], x[-1], h_grafico)
    yl = np.zeros_like(xl)
    for i in range(xl.shape[0]):
        aux = 0
        for j in range(a.shape[0]):
            aux += a[j]*xl[i]**(j)
        yl[i] = aux

    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')
    ax.plot(xl, yl)

    ax.set(xlabel='x', ylabel='y')
    ax.grid()

    fig.savefig("newton.png")
    plt.show()

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    pontos = []
    predict = False
    for l in input_file:
        l = l.split()
        l = [float(i) for i in l]
        if len(l) == 2:
            pontos.append(l)
        # predicao
        elif len(l) > 2:
            predict = True
            a = l
    
    if predict:
        a = np.asarray(a)
        y = predicao(a[:-1], a[-1])
        output_file.write(str(y))
    else:
        pontos = np.asarray(pontos)
        a = newton(pontos)

        for i in range(a.shape[0]):
            output_file.write("a"+str(i)+" = "+str(a[i])+"\n")

        mostrar_grafico(pontos, a)
    
    input_file.close()
    output_file.close()

main()