import numpy as np
from utils import solve_func

# 2 a 6
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

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    for l in input_file:
        l = l.split()
        funcao = l[0]
        a = float(l[1])
        b = float(l[2])
        pontos = int(l[3])
    
    i = quadratura_gauss(funcao, a, b, pontos)

    output_file.write(str(i))

    input_file.close()
    output_file.close()

main()