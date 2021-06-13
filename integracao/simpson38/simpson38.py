import numpy as np

# como verificar número válido de pontos?
# intervalo igual entre os pontos
# verificar
def simpson38(pontos):
    # pontos ordenados por x
    x = pontos[:, 0]
    y = pontos[:, 1]
    p = len(x)  # numero de pontos

    # verificação do número de pontos
    if (p < 4) or ((p-4) % 3 != 0):
        print("Erro! Número de pontos inválido!")
        return 0

    n = (p-1)/3 # numero de vezes que dá pra aplicar simpson

    i = 0
    for j in range(1, p-1, 3):
        i += 3*y[j]
        i += 3*y[j+1]
    for j in range(3, p-3, 3):
        i += 2*y[j]
    i += y[0]
    i += y[p-1]
    i *= abs(x[0]-x[p-1]) # multiplicar pela largura
    i /= 8*n # dividir pelo numero de vezes que aplicamos simpson

    print(i)
    return i

p1 = [[0, 0.2], [0.2667, 1.432724], [0.5333, 3.487177], [0.8, 0.232]]
p2 = [[0, 0.2], [0.2, 1.288], [0.4, 2.456], [0.6, 3.464], [0.8, 0.232]]
p1 = np.asarray(p1)
p2 = np.asarray(p2)
simpson38(p1)
simpson38(p2)