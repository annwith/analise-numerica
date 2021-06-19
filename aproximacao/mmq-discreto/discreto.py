'''
Aproximação Polinomial
Método dos Mínimos Quadrados
'''
import numpy as np
import matplotlib.pyplot as plt

def eliminacao_gauss(m):
    for i in range(0, m.shape[0]-1):
        sub = m[i+1:, i] / m[i][i]
        for j in range(i, m.shape[0]-1):
            m[j+1, :] = m[j+1, :] - sub[j-i]*m[i, :]

    x = []
    for i in range(m.shape[0]-1, -1, -1):
        x.append((m[i][-1] - np.sum(m[i, i+1:-1])) / m[i][i])
        m[:, i] *= x[-1]

    return np.flip(x)

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

    fig.savefig("discreto.png")
    plt.show()

def discreto(pontos, m):
    pontos = np.asarray(pontos)
    x = pontos[:, 0]
    y = pontos[:, 1]

    # Base vetorial
    p = []
    for i in range(m+1):
        p.append(x**i)

    p = np.asarray(p)
    # print(p)

    matriz = np.zeros((m+1, m+2))
    ly = np.zeros((m+1))

    for i in range(m+1):
        ly[i] =  np.sum(y*p[i])
        for j in range(m+1):
            matriz[i][j] = np.sum(p[i]*p[j])

    # print(matriz)
    # print(ly)

    for i in range(ly.shape[0]):
        matriz[i][-1] = ly[i]

    # print(matriz)

    a = eliminacao_gauss(matriz)
    # print(a)

    return a

def predicao(a, x):
    y = 0
    for j in range(a.shape[0]):
        y += a[j]*x**(j)
    return y

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    pontos = []
    predict = False
    for l in input_file:
        l = l.split()
        l = [float(i) for i in l]
        if len(l) == 1:
            m = int(l[0])
        elif len(l) == 2:
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
        a = discreto(pontos, m)

        for i in range(a.shape[0]):
            output_file.write("a"+str(i)+" = "+str(a[i])+"\n")

        mostrar_grafico(pontos, a)
    
    input_file.close()
    output_file.close()

main()