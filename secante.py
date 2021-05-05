import math
import numpy as np
from utils import solve_func

def secante(funcao, a, b, precisao):
    # se a maior que b: trocar
    if a > b:
        [a, b] = [b, a]

    iteracao = 0
    f_a = solve_func(a, funcao)
    f_b = solve_func(b, funcao)
    it = []

    it.append([a, f_a])
    it.append([b, f_b])

    # Limite de vezes seguidas que a(k)-a(k-1) > a(k-1)-a(k-2)
    limite = 0

    # Inicialização
    f_x_2 = f_a
    while(abs(f_x_2) > precisao):
        iteracao += 1

        # Atualização do ponto de acordo com a funcao de convergencia
        x_1 = it[-1][0]
        f_x_1 = it[-1][1]
        x_0 = it[-2][0]
        f_x_0 = it[-2][1]
        x_2 = (f_x_1*x_0 - f_x_0*x_1) / (f_x_1 - f_x_0)
        f_x_2 = solve_func(x_2, funcao)
        it.append([x_2, f_x_2])

        # Verificar se está convergindo
        d_anterior = abs(it[iteracao-2][0]-it[iteracao-1][0])
        d_atual = abs(it[iteracao-1][0]-it[iteracao][0])

        if d_anterior < d_atual:
            limite += 1
        else:
            limite = 0
            
        if limite == 4:
            None, None
    
    return x_2, it

def main():
    input_txt = open('input-secante.txt', 'r')
    output_txt = open('output-secante.txt', 'w')
    np.set_printoptions(precision=6)
    np.set_printoptions(suppress=True)

    for line in input_txt:
        if line[-1] == '\n':
            line = line[:-1]
        # output_txt.write(line+' ')
        line = line.split(',')
        func = line[0].split('=')[1]
        a = float(line[1].split('=')[1])
        b = float(line[2].split('=')[1])
        precisao = float(line[3].split('=')[1])

        x, iteracoes = secante(func, a, b, precisao)
        if x != None:
            iteracoes = np.asarray(iteracoes)
            f_x = solve_func(x, func)
            x = np.asarray([x])
            f_x = np.asarray([f_x])
            output_txt.write("iteracoes="+str(len(iteracoes))+",x="+str(x)+",f(x)="+str(f_x)+'\n')
        else:
            print("intervalo inválido")
            output_txt.write("intervalo invalido\n")

    input_txt.close()
    output_txt.close()

main()