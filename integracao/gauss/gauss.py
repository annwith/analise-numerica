import numpy as np
from utils import solve_func

def quadratura_gauss(funcao, a, b, pontos):
    clist = [[1, 1]]
    xlist = [[-1/3**0.5, 1/3**0.5]]

    # garantir a < b
    if a > b:
        a, b = b, a

    cte = (b+a)/2
    x = (b-a)/2
    dx = (b-a)/2

    funcao = funcao.replace("x", "("+str(cte)+"+"+str(x)+"*x)")
    funcao = "("+funcao+")*"+str(dx)
    print(funcao)

    for i in range(pontos):
        xlist[pontos-2][i] = solve_func(xlist[pontos-2][i], funcao)

    clist = np.asarray(clist)
    xlist = np.asarray(xlist)
    i = np.sum(clist[pontos-2]*xlist[pontos-2])

    print(i)
    return i


funcao = "0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5"
quadratura_gauss(funcao, 0, 0.8, 2)