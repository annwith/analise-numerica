import math
import numpy as np
from utils import solve_func

# Definir o número de casas de precisão pra fazer os cálculos
# Verificação de loop infinito? Limite de iterações?
def posicao_falsa(funcao, a, b, precisao):
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
    
    repeat = False
    if (abs(f_a) > precisao and abs(f_b) > precisao):
        repeat = True

    # Loop
    while(repeat and a < b):
        iteracao += 1

        # Escolher 0 entre pontos a e b
        # f_b - f_a != 0 (TRATAR ISSO)
        c = (a*f_b-b*f_a)/(f_b-f_a)
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

        repeat = False
        if (abs(f_a) > precisao and abs(f_b) > precisao):
            repeat = True
    
    return c, it

def main():
    input_txt = open('input-pos-falsa.txt', 'r')
    output_txt = open('output-pos-falsa.txt', 'w')

    for line in input_txt:
        output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        a = float(line[1].split('=')[1])
        b = float(line[2].split('=')[1])
        precisao = float(line[3].split('=')[1])

        x, iteracoes = posicao_falsa(func, a, b, precisao)
        iteracoes = np.asarray(iteracoes)
        print(iteracoes)
        output_txt.write("iteracoes="+str(len(iteracoes))+",resultado="+str(x)+'\n')

    input_txt.close()
    output_txt.close()

main()