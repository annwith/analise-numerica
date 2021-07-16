from utils import *
import math
import numpy as np
import matplotlib.pyplot as plt

# método iterativo
def heun_method(funcao, x_i, x_f, y_i, h):
    pontos = []
    pontos.append([x_i, y_i])

    # iterar até a diferença entre as iterações diminuir
    while(x_i < x_f):
        f_1 = solve_dif_func(x_i, y_i, funcao)
        y_i_1 = y_i + f_1*h
        x_i_1 = x_i + h
        y_i_ant = math.inf
        
        i = 0
        for i in range(15):
            y_i_ant = y_i_1
            f_2 = solve_dif_func(x_i_1, y_i_1, funcao)*h
            y_i_1 = y_i + ((f_1+f_2)/2)*h
            if i > 14:
                print(i)
                break
            i += 1
        
        y_i = y_i_1
        x_i += h
        pontos.append([x_i, y_i])

    return np.asarray(pontos)

# retorna apenas o proximo valor
def heun(func, variables, values, i, h):
    # iterar até a diferença entre as iterações diminuir
    f1 = solve_diferential_function(variables, values, func)
    preditor = values[i] + f1*h
    aux = values.copy()
    aux[0] = values[0] + h # x
    aux[i] = preditor      # variavel em questao
    f2 = solve_diferential_function(variables, aux, func)
    corretor = values[i] + ((f1+f2)/2)*h
    compar = preditor
    c = 0
    # qual diferença isso realmente faz?
    while(abs(corretor-compar)>0.01):
        compar = corretor
        aux[i] = corretor
        f2 = solve_diferential_function(variables, aux, func)*h
        corretor = values[i] + ((f1+f2)/2)*h
        if c > 20:
            break
        c += 1

    return corretor

def solve_system_heun(functions, variables, values, x_f, h):
    pontos = []
    for value in values:
        pontos.append(value)
    
    while(values[0] < x_f):
        i = 1
        aux = []
        for func in functions:
            # heun method
            aux.append(heun(func, variables, values, i, h))
            i += 1
        # só atualiza os valores juntos
        for i in range(len(aux)):
            values[i+1] = aux[i]
        values[0] += h # x
        for value in values:
            pontos.append(value)
    
    pontos = np.asarray(pontos)
    pontos = np.reshape(pontos, (int(len(pontos)/len(values)), len(values)))

    return pontos

# nao faz muito sentido
def grade_adaptativa(funcao, x_i, x_f, y_i, h, dif_y):
    pontos = []
    pontos.append([x_i, y_i])

    while(x_i < x_f):
        y_i = pontos[-1][1] 
        h_i = h
        p = heun(funcao, x_i, x_i+h, y_i, h)
        y_ant = p[-1][1]
        h_i = h_i/2
        p = heun(funcao, x_i, x_i+h, y_i, h_i)
        y_f = p[-1][1]
        while(abs(y_ant-y_f)>dif_y):
            y_ant = y_f
            print(y_ant-y_f)
            print(h_i)
            h_i = h_i/2
            p = heun(funcao, x_i, x_i+h, y_i, h_i)
            y_f = p[-1][1]
        x_i += h
        for i in range(1, len(p)):
            pontos.append(p[i])

    return pontos

def mostrar_grafico(pontos):
    pontos = np.asarray(pontos)
    # Data for plotting
    x = pontos[:, 0]
    y = pontos[:, 1]

    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')

    ax.set(xlabel='x', ylabel='y')
    ax.grid()

    fig.savefig("image.png")
    plt.show()

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    lines = input_file.readlines()
    functions = lines[0].split()
    variables = lines[1].split()
    initial_values = lines[2].split()
    for i in range(len(initial_values)):
        initial_values[i] = float(initial_values[i])
    xf = float(lines[3].split()[0])
    h = float(lines[4].split()[0])
    
    pontos = solve_system_heun(functions, variables, initial_values, xf, h)
    print(pontos)
    mostrar_grafico(pontos)

    output_file.write(str(pontos[-1][1])+"\n")

    input_file.close()
    output_file.close()

main()

