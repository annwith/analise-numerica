import numpy as np
import matplotlib.pyplot as plt

# quando adiciona um ponto tem que fazer tudo de novo
def lagrange(pontos):
    x = pontos[:, 0]
    y = pontos[:, 1]
    n = len(x) # numero de pontos

    # print(x)
    # print(y)

    l = np.zeros((n, n-1, 2), dtype=np.float64)
    divisor = np.ones((n), dtype=np.float64)

    # Todos os agrupamentos de x-1 possível (x agrupamentos)
    for i in range(n):
        ind = 0
        for j in range(n):
            if i != j:
                # (x-1)(x-5)(x-6)
                l[i][ind][0] = -x[j]  # grau 0
                l[i][ind][1] = 1        # grau 1
                divisor[i] *= x[i]-x[j]
                ind += 1

    # print(l)
    # print(divisor)

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

    p = []
    for i in range(n):
        p.append(l[i][0])

    for i in range(n):
        for j in range(1, l.shape[1]):
            p[i] = mul(p[i], l[i][j])
    
    p = np.asarray(p)
    # print(p)

    # dividindo os polinomios pelo valor que eles devem ser divididos
    for i in range(n):
        p[i] /= divisor[i]
        # p[i] *= y[i]

    # print(p)

    # multiplicando os polinomios por y
    for i in range(n):
        p[i] *= y[i]

    # print(p)

    # fazendo a soma
    p = np.sum(p, axis=0)
    # print(p)

    return p

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

    fig.savefig("lagrange.png")
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
        a = lagrange(pontos)

        for i in range(a.shape[0]):
            output_file.write("a"+str(i)+" = "+str(a[i])+"\n")

        mostrar_grafico(pontos, a)
    
    input_file.close()
    output_file.close()

main()