import math
import numpy as np
from utils import solve_func

def newton_raphson(funcao, f_der, a, precisao):
    iteracao = 0
    f_a = solve_func(a, funcao)
    it = []

    it.append([a, f_a])

    # Limite de vezes seguidas que a(k)-a(k-1) > a(k-1)-a(k-2)
    limite = 0

    while(abs(f_a) > precisao):
        iteracao += 1

        # Atualização do ponto de acordo com a funcao de convergencia
        print(solve_func(a, f_der))
        a = a - solve_func(a, funcao)/solve_func(a, f_der)
        f_a = solve_func(a, funcao)
        it.append([a, f_a])

        # Verificar se está convergindo
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
    input_txt = open('input-newton.txt', 'r')
    output_txt = open('output-newton.txt', 'w')

    for line in input_txt:
        output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        print(func)
        f_der = line[1].split('=')[1]
        print(f_der)
        a = float(line[2].split('=')[1])
        precisao = float(line[3].split('=')[1])

        x, iteracoes = newton_raphson(func, f_der, a, precisao)
        iteracoes = np.asarray(iteracoes)
        print(iteracoes)
        output_txt.write("iteracoes="+str(len(iteracoes))+",resultado="+str(x)+'\n')

    input_txt.close()
    output_txt.close()

main()