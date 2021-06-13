import math
import numpy as np
from utils import solve_func

def ponto_fixo(funcao, f_conv, a, precisao):
    iteracao = 0
    f_a = solve_func(a, funcao)
    it = []

    it.append([a, f_a])

    # Limite de vezes seguidas que a(k)-a(k-1) > a(k-1)-a(k-2)
    limite = 0

    while(abs(f_a) > precisao):
        iteracao += 1

        # Atualização do ponto de acordo com a funcao de convergencia
        a = solve_func(a, f_conv)
        f_a = solve_func(a, funcao)
        it.append([a, f_a])

        if iteracao > 1:
            d_anterior = abs(it[iteracao-2][0]-it[iteracao-1][0])
            d_atual = abs(it[iteracao-1][0]-it[iteracao][0])

            if d_anterior < d_atual:
                limite += 1
            else:
                limite = 0
            
        if limite == 4:
            break
    
    return a, it

def main():
    input_txt = open('input-ponto-fixo.txt', 'r')
    output_txt = open('output-ponto-fixo.txt', 'w')

    for line in input_txt:
        output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        f_conv = line[1].split('=')[1]
        a = float(line[2].split('=')[1])
        precisao = float(line[3].split('=')[1])

        x, iteracoes = ponto_fixo(func, f_conv, a, precisao)
        iteracoes = np.asarray(iteracoes)
        print(iteracoes)
        output_txt.write("iteracoes="+str(len(iteracoes))+",resultado="+str(x)+'\n')

    input_txt.close()
    output_txt.close()

main()