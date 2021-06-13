'''
Aproximação Polinomial
Método dos Mínimos Quadrados
'''
import numpy as np

def discreto(pontos, m):
    pontos = np.asarray(pontos)
    x = pontos[:, 0]
    y = pontos[:, 1]

    print(x)
    print(y)

    # Base vetorial
    p = []
    for i in range(m+1):
        p.append(x**i)

    p = np.asarray(p)
    print(p)

    matriz = np.zeros((m+1, m+1))
    ly = np.zeros((m+1))

    for i in range(m+1):
        ly[i] =  np.sum(y*p[i])
        for j in range(m+1):
            matriz[i][j] = np.sum(p[i]*p[j])

    print(matriz)
    print(ly)

    # Resolver esse sistema linear
    # Gauss, LU, Jacobi, Gauss-Seidel
    # Verificar qual método utilizar
    # Fazer verificações sobre a matriz
    # Pivoteamento, Etc

    # Testar o resultado final

pontos = [[-1, 0], [0, -1], [1, 0], [2, 7]]

discreto(pontos, 2)