import numpy as np
from utils import solve_func

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
        i = simpson13(pontos)
    else:
        pontos = np.asarray(pontos)
        i = simpson13(pontos)

    output_file.write(str(i))

    input_file.close()
    output_file.close()

main()