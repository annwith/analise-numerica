import math
import numpy as np
from utils import solve_func
from utils import intervalo_zero

# Definir o número de casas de precisão pra fazer os cálculos
# Verificação de loop infinito? Limite de iterações?
def posicao_falsa(funcao, a, b, precisao):
    # Garantir que existe uma raíz nesse intervalo
    if not intervalo_zero(funcao, a, b):
        return None, None

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
    while(repeat and abs(a-b) > 10**-12):
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
        print("a "+str(a))
        print("b "+str(b))
        print(str(f_a))
        print(str(f_b))

        repeat = False
        if (abs(f_a) > precisao and abs(f_b) > precisao):
            repeat = True
    
    return c, it

def main():
    input_txt = open('input-pos-falsa.txt', 'r')
    output_txt = open('output-pos-falsa.txt', 'w')

    for line in input_txt:
        if line[-1] == '\n':
            line = line[:-1]
        output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        a = float(line[1].split('=')[1])
        b = float(line[2].split('=')[1])
        precisao = float(line[3].split('=')[1])

        x, iteracoes = posicao_falsa(func, a, b, precisao)
        iteracoes = np.asarray(iteracoes)
        print(iteracoes)
        f_x = solve_func(x, func)
        output_txt.write("iteracoes="+str(len(iteracoes))+",x="+str(x)+",f(x)="+str(f_x)+'\n')
    
    input_txt.close()
    output_txt.close()

main()