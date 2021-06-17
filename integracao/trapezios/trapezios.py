import numpy as np
from utils import solve_func

# o erro cai devagar nesse método
# qualquer numero de pontos > 1
# funciona para trapezios simples e multiplos, e com hs diferentes
def trapezios(pontos):
    # pontos ordenados por x
    x = pontos[:, 0]
    y = pontos[:, 1]
    n = len(x)

    if n == 1:
        print("Erro! Intervalo inválido!")
        return 0

    # calcular area
    i = 0
    # escolhi fazer assim pq funcionaria para um h diferente
    for j in range(0, n-1):
        i += (y[j] + y[j+1])*abs(x[j] - x[j+1])/2

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
        i = trapezios(pontos)
    else:
        pontos = np.asarray(pontos)
        i = trapezios(pontos)

    output_file.write(str(i))

    input_file.close()
    output_file.close()

main()