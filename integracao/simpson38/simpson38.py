import numpy as np
from utils import solve_func

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

    return i

# recebe a funcao, a e b e o numero de segmentos
# retorna os pontos
def funcao_pontos(funcao, a, b, segmentos):
    # garantir a < b
    if a > b:
        a, b = b, a

    pontos = []
    h = abs(a-b)/(segmentos)

    pontos.append([a, solve_func(a, funcao)])
    for i in range(1, segmentos):
        pontos.append([a+i*h, solve_func(a+i*h, funcao)])
    pontos.append([b, solve_func(b, funcao)])

    return pontos

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    pontos = []
    funcao = False
    for l in input_file:
        if l == "funcao\n":
            funcao = True
            continue
        if not funcao:
            l = l.split()
            l = [float(i) for i in l]
            pontos.append(l)
        else:
            l = l.split()
            funcao = l[0]
            a = float(l[1])
            b = float(l[2])
            segmentos = int(l[3])
    
    if funcao:
        pontos = funcao_pontos(funcao, a, b, segmentos)
        pontos = np.asarray(pontos)
        i = simpson38(pontos)
    else:
        pontos = np.asarray(pontos)
        i = simpson38(pontos)

    output_file.write(str(i))

    input_file.close()
    output_file.close()

main()