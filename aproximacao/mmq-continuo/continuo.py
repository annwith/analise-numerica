import numpy as np
from utils import solve_func

def continuo(funcao, a, b, grau):
    # garantir a < b
    if a > b:
        a, b = b, a

    matriz = np.zeros((grau+1, grau+1))
    e = 1
    for i in range(grau+1):
        for j in range(grau+1):
            exp = e+j
            matriz[i][j]=b**exp/exp-a**exp/exp
        e += 1

    print(matriz)

    ly = np.zeros(grau+1)
    # Como calcular a integral definida?

    # Usar eliminação de Gauss depois

    # Testar o resultado final


        
funcao = "x**4-5*x"
continuo(funcao, -1, 1, 2)