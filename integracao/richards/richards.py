import numpy as np
from utils import solve_func

# fácil de escolher intervalos e bom, pouca diferença pro 38
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
def romberg(funcao, a, b, lista_segmentos):
    r = np.zeros((len(lista_segmentos), len(lista_segmentos)))
    h = []
    for i in range(len(lista_segmentos)):
        pontos, distancia = funcao_pontos(funcao, a, b, lista_segmentos[i]) # retorna [pontos, h]
        r[i][0] = simpson13(np.asarray(pontos)) # passa os pontos para uma funcao de integração)
        h.append(distancia)
 
    # print(h)
    # print(np.asarray(r))

    # finalizar construção da arvore
    for i in range(1, r.shape[0]):
        for j in range(r.shape[0]-i):
            r[j][i] = richards(r[j][i-1], h[j], r[j+1][i-1], h[j+i])

    print(r)

    return r[0][-1]

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    segmentos = []
    for l in input_file:
        l = l.split()
        funcao = l[0]
        a = float(l[1])
        b = float(l[2])
        for i in range(3, len(l)):
            segmentos.append(int(l[i]))
    
    i = romberg(funcao, a, b, segmentos)

    output_file.write(str(i))

    input_file.close()
    output_file.close()

main()

# a ordem dos segmentos importa?
# é possível tirar e colocar segmentos? se sim só da ultima posicao, como uma pilha correto?
# o tipo de integração importa? eu posso fazer simpson com trapézio e tudo bem?