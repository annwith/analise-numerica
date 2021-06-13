import numpy as np

# o erro cai devagar nesse método
# qualquer numero de pontos > 1
# funciona para trapezios simples e multiplos, e com hs diferentes
def trapezios(pontos):
    # pontos ordenados por x
    x = pontos[:, 0]
    y = pontos[:, 1]
    n = len(x)

    # e se houverem pontos cujo y é negativo?
    
    # calcular area
    i = 0
    # escolhi fazer assim pq funcionaria para um h diferente
    for j in range(0, n-1):
        i += (y[j] + y[j+1])*abs(x[j] - x[j+1])/2

    print(i)

p1 = [[0, 0.2], [0.4, 2.456], [0.8, 0.232]]
p2 = [[0, 0.2], [0.2, 1.288], [0.4, 2.456], [0.6, 3.464], [0.8, 0.232]]
p1 = np.asarray(p1)
p2 = np.asarray(p2)
trapezios(p1)
trapezios(p2)