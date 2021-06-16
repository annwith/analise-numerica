import numpy as np
from utils import solve_func

def trapezios(pontos):
    # pontos ordenados por x
    x = pontos[:, 0]
    y = pontos[:, 1]
    p = len(x)

    if p == 1:
        print("Erro! Intervalo inválido!")
        return 0

    # e se houverem pontos cujo y é negativo?
    
    # calcular area
    i = 0
    # escolhi fazer assim pq funcionaria para um h diferente
    for j in range(0, p-1):
        i += (y[j] + y[j+1])*abs(x[j] - x[j+1])/2

    return i

# aqui tem escolhas de implementação a serem feitas
def richards(i1, h1, i2, h2):
    # garantir h1 > h2 (não sei ainda pq)
    # trocar por valor, não trocar os valores do vetor que estou passando
    # pois a ordem faz diferença para construir a arvore

    x1 = i1
    x2 = i2
    y1 = h1
    y2 = h2

    if y1 < y2:
        y1, y2 = y2, y1
        x1, x2 = x2, x1

    return x2 + (1/((y1/y2)**2-1)) * (x2-x1)

# n é um numero
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

    return pontos, h

# n é uma lista de numeros de pontos
# ou seria a integração de romberg (reaproveitamento de richards)
def arvore_richards(funcao, a, b, lista_segmentos):
    r = np.zeros((len(lista_segmentos), len(lista_segmentos)))
    h = []
    for i in range(len(lista_segmentos)):
        pontos, distancia = funcao_pontos(funcao, a, b, lista_segmentos[i]) # retorna [pontos, h]
        r[i][0] = trapezios(np.asarray(pontos)) # passa os pontos para uma funcao de integração)
        h.append(distancia)
 
    print(h)
    print(np.asarray(r))

    # finalizar construção da arvore
    for i in range(1, r.shape[0]):
        for j in range(r.shape[0]-i):
            r[j][i] = richards(r[j][i-1], h[j], r[j+1][i-1], h[j+i])

    print(r)

    return r, h

# faz a melhor integração possível dados os pontos
# def integracao():

# adiciona mais um h na árvore
# def add_arvore(arvore, i, h):

funcao = "0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5"
arvore_richards(funcao, 0, 0.8, [1, 2, 4, 8])

# a ordem dos segmentos importa?
# é possível tirar e colocar segmentos? se sim só da ultima posicao, como uma pilha correto?
# o tipo de integração importa? eu posso fazer simpson com trapézio e tudo bem?