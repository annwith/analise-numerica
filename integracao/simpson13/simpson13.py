import numpy as np

# numero impar de pontos > 1
# intervalo igual entre os pontos
# verificar
def simpson13(pontos):
    # pontos ordenados por x
    x = pontos[:, 0]
    y = pontos[:, 1]
    p = len(x)  # numero de pontos

    # verificar numero impar de pontos
    if p == 1 or p % 2 == 0:
        print("Erro! Intervalo inválido!")
        return 0

    # explicar como escolhi achar o n
    n = (p-1)/2 # numero de vezes que dá pra aplicar simpson

    i = 0
    for j in range(1, p-1, 2):
        i += 4*y[j] 
    for j in range(2, p-2, 2):
        i += 2*y[j]
    i += y[0]
    i += y[p-1]
    i *= abs(x[0]-x[p-1])
    i /= 6*n

    print(i)
    return i

p1 = [[0, 0.2], [0.4, 2.456], [0.8, 0.232]]
p2 = [[0, 0.2], [0.2, 1.288], [0.4, 2.456], [0.6, 3.464], [0.8, 0.232]]
p1 = np.asarray(p1)
p2 = np.asarray(p2)
simpson13(p1)
simpson13(p2)