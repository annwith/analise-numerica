import numpy as np
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

def quadratura_gauss(funcao, a, b, pontos=4):
    clist = [[0.3478548, 0.6521452, 0.6521452, 0.3478548]]
    xlist = [[-0.861136312, -0.339981044, 0.339981044, 0.861136312]]

    # garantir a < b
    if a > b:
        a, b = b, a

    cte = (b+a)/2
    x = (b-a)/2
    dx = (b-a)/2

    funcao = funcao.replace("x", "("+str(cte)+"+"+str(x)+"*x)")
    funcao = "("+funcao+")*"+str(dx)

    for i in range(pontos):
        xlist[pontos-4][i] = solve_func(xlist[pontos-4][i], funcao)

    clist = np.asarray(clist)
    xlist = np.asarray(xlist)
    i = np.sum(clist[pontos-4]*xlist[pontos-4])

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
    # PRODUTO ESCALAR ENTRE FUNÇÕES
    f = []
    for i in range(0, grau+1):
        f.append("("+funcao+")*x^"+str(i))

    print(f)

    for i in range(len(f)):
        f[i] = quadratura_gauss(f[i], a, b)
        matriz[i][-1] = f[i]

    # print(matriz)

    a = eliminacao_gauss(matriz)
    # Testar o resultado final
    # print(a)
    return a

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    for l in input_file:
        l = l.split()
        funcao = l[0]
        a = float(l[1])
        b = float(l[2])
        grau = int(l[3])
    
    a = continuo(funcao, a, b, grau)

    for i in range(a.shape[0]):
        output_file.write("a"+str(i)+" = "+str(a[i])+"\n")

    input_file.close()
    output_file.close()

main()