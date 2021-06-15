import numpy as np
from utils import solve_func

def trapezios(pontos):
    # pontos ordenados por x
    x = pontos[:, 0]
    y = pontos[:, 1]
    n = len(x)

    if p == 1:
        print("Erro! Intervalo inválido!")
        return 0

    # e se houverem pontos cujo y é negativo?
    
    # calcular area
    i = 0
    # escolhi fazer assim pq funcionaria para um h diferente
    for j in range(0, n-1):
        i += (y[j] + y[j+1])*abs(x[j] - x[j+1])/2

    return i

# aqui tem escolhas de implementação a serem feitas
def richards(i1, h1, i2, h2):
    # garantir h1 > h2 (não sei ainda pq)
    if h1 < h2:
        h1, h2 = h2, h1
        i1, i2 = i2, i1

    return i2 + (1/((h1/h2)**2-1)) * (i2-i1)

print(richards(0.1728, 0.8, 1.0688, 0.4))

# n é um numero
def funcao_pontos(funcao, a, b, segmentos):
    # garantir a < b
    if a > b:
        a, b = b, a

    pontos = []
    h = abs(a-b)/(segmentos+1)

    pontos.append([a, solve_func(a, funcao)])
    for i in range(1, segmentos):
        pontos.append([a+i*h, solve_func(a+i*h, funcao)])
    pontos.append([b, solve_func(b, funcao)])

    return pontos, h

# n é uma lista de numeros de pontos
def arvore_richards(funcao, a, b, n):
    r = []
    for i in range(len(n)):
        r.append(funcao_pontos(funcao, a, b, n[i])) # retorna [pontos, h]

    print(r)

    # inicialização com um método de integração
    for i in range(len(r)):
        r[i][0] = trapezios(r[i][0])

    print(r)

    # finalizar construção da arvore

arvore_richards()