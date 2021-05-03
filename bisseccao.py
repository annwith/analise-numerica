import math
import numpy as np
from utils import solve_func

# Definir o número de casas de precisão pra fazer os cálculos
# Verificação de loop infinito? Limite de iterações?
def bisseccao(funcao, a, b, precisao=None, distancia_absoluta=None, distancia_relativa=None):
    # Garantir a < b e a != b
    if a > b:
        [a, b] = [b, a]
    elif a == b:
        return "Interval Error"

    # Inicialização
    it = []

    iteracao = 0
    f_a = solve_func(a, funcao)
    f_b = solve_func(b, funcao)
    d_absoluta = abs(a-b)
    if a != 0:
        d_relativa = abs((a-b)/a)
    else:
        d_relativa = None
    
    it.append([iteracao, a, b, f_a, f_b, d_absoluta, d_relativa])
    
    # Verificação de condição de parada (precisão/distância)
    # Se houver mais de uma condição, todas devem ser satisfeitas
    repeat = False
    if (distancia_absoluta != None and d_absoluta > distancia_absoluta):
        repeat = True
    if (a != 0 and distancia_relativa != None and d_relativa > distancia_relativa):
        repeat = True
    if (precisao != None and abs(f_a) > precisao and abs(f_b) > precisao):
        repeat = True

    # Loop
    while(repeat and a < b):
        iteracao += 1

        # Escolher uma metade
        c = (a+b)/2
        f_c = solve_func(c, funcao)

        if f_a*f_c < 0:
            b = c
            f_b = solve_func(b, funcao)
        else:
            a = c
            f_a = solve_func(a, funcao)
        
        d_absoluta = abs(a-b)
        if a != 0:
            d_relativa = abs((a-b)/a)
        else:
            d_relativa = None

        it.append([iteracao, a, b, f_a, f_b, d_absoluta, d_relativa])

        # Verificação de condição de parada (precisão/distância)
        # Se houver mais de uma condição, todas devem ser satisfeitas
        repeat = False
        if (distancia_absoluta != None and d_absoluta > distancia_absoluta):
            repeat = True
        if (a != 0 and distancia_relativa != None and d_relativa > distancia_relativa):
            repeat = True
        if (precisao != None and abs(f_c) > precisao):
            repeat = True
    
    return c, it

# Definir o número de iterações necessárias
def iteracoes_bisseccao(a, b, distancia_absoluta):
    i = abs(a-b)
    n = (math.log(i)-math.log(distancia_absoluta))/math.log(2)
    return n

def main():
    input_txt = open('input-bisec.txt', 'r')
    output_txt = open('output-bisec.txt', 'w')

    for line in input_txt:
        output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        a = float(line[1].split('=')[1])
        b = float(line[2].split('=')[1])
        precisao = line[3].split('=')[1]
        distancia_absoluta = line[4].split('=')[1]
        distancia_relativa = line[5].split('=')[1]
        if precisao == 'None':
            precisao=None
        else:
            precisao = float(line[3].split('=')[1])
        if distancia_absoluta == 'None':
            distancia_absoluta=None
        else:
            distancia_absoluta = float(line[4].split('=')[1])
        if distancia_relativa == 'None':
            distancia_relativa=None
        else:
            distancia_relativa = float(line[5].split('=')[1])

        x, iteracoes = bisseccao(func, a, b, precisao, distancia_absoluta, distancia_relativa)
        iteracoes = np.asarray(iteracoes)
        print(iteracoes)
        output_txt.write("iteracoes="+str(len(iteracoes))+",resultado="+str(x)+'\n')

    input_txt.close()
    output_txt.close()

main()