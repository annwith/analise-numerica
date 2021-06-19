import numpy as np
import matplotlib.pyplot as plt
from utils import solve_func

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

def quadratura_gauss(funcao, a, b, pontos):
    clist = [[1, 1], 
            [0.5555556, 0.8888889, 0.5555556],
            [0.3478548, 0.6521452, 0.6521452, 0.3478548],
            [0.2369269, 0.4786287, 0.5688889, 0.4786287, 0.2369269],
            [0.1713245, 0.3607616, 0.4679139, 0.4679139, 0.3607616, 0.1713245]]
    xlist = [[-1/3**0.5, 1/3**0.5],
            [-0.774596669, 0, 0.774596669],
            [-0.861136312, -0.339981044, 0.339981044, 0.861136312],
            [-0.906179846, -0.538469310, 0, 0.538469310, 0.906179846],
            [-0.932469514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.932469514]]

    # garantir a < b
    if a > b:
        a, b = b, a

    cte = (b+a)/2
    x = (b-a)/2
    dx = (b-a)/2

    funcao = funcao.replace("x", "("+str(cte)+"+"+str(x)+"*x)")
    funcao = "("+funcao+")*"+str(dx)

    for i in range(pontos):
        xlist[pontos-2][i] = solve_func(xlist[pontos-2][i], funcao)

    i = np.sum(np.asarray(clist[pontos-2])*np.asarray(xlist[pontos-2]))

    return i

def continuo(funcao, a, b, grau):
    # garantir a < b
    if a > b:
        a, b = b, a

    matriz = np.zeros((grau+1, grau+2))
    e = 1
    for i in range(grau+1):
        for j in range(grau+1):
            exp = e+j
            matriz[i][j]=b**exp/exp-a**exp/exp
        e += 1

    # print(matriz)
    # Como calcular a integral definida?
    f = []
    for i in range(0, grau+1):
        f.append("("+funcao+")*x^"+str(i))

    # print(f)

    for i in range(len(f)):
        f[i] = quadratura_gauss(f[i], a, b, 6)
        matriz[i][-1] = f[i]

    # print(matriz)

    a = eliminacao_gauss(matriz)
    # Testar o resultado final
    # print(a)
    return a

def mostrar_grafico(funcao, a, i, f):
    # Data for plotting
    h_grafico = abs(i-f)/100
    x = np.arange(i, f, h_grafico)
    y1 = np.zeros_like(x)
    for i in range(x.shape[0]):
        y1[i] = solve_func(x[i], funcao)

    # Data for plotting
    y2 = np.zeros_like(x)
    for i in range(x.shape[0]):
        aux = 0
        for j in range(a.shape[0]):
            aux += a[j]*x[i]**(j)
        y2[i] = aux

    fig, ax = plt.subplots()
    ax.plot(x, y1, color='b')
    ax.plot(x, y2, color='g')

    ax.set(xlabel='x', ylabel='y')
    ax.grid()

    fig.savefig("continuo.png")
    plt.show()

def predicao(a, x):
    y = 0
    for j in range(a.shape[0]):
        y += a[j]*x**(j)
    return y

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    predict = False
    for l in input_file:
        if l == 'inferencia\n':
            predict = True
            continue
        if predict:
            l = l.split()
            l = [float(i) for i in l]
            p = l
        else:
            l = l.split()
            funcao = l[0]
            a = float(l[1])
            b = float(l[2])
            grau = int(l[3])
    
    if predict:
        p = np.asarray(p)
        y = predicao(p[:-1], p[-1])
        output_file.write(str(y))
    else:
        p = continuo(funcao, a, b, grau)

        for i in range(p.shape[0]):
            output_file.write("a"+str(i)+" = "+str(p[i])+"\n")
        
        mostrar_grafico(funcao, p, a, b)

    input_file.close()
    output_file.close()

main()