from utils import *
import numpy as np
import matplotlib.pyplot as plt

# solves ordinary equation
def euler(funcao, x_i, x_f, y_i, h):
    pontos = []
    pontos.append([x_i, y_i])

    while(x_i < x_f):
        y_i = y_i + solve_dif_func(x_i, y_i, funcao)*h
        x_i += h
        pontos.append([x_i, y_i])

    return pontos

def solve_system_euler(functions, variables, values, x_f, h):
    pontos = []
    for value in values:
        pontos.append(value)
    
    while(values[0] < x_f):
        i = 1
        aux = []
        for func in functions:
            # euler method
            aux.append(values[i] + solve_diferential_function(variables, values, func)*h)
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
    
    pontos = solve_system_euler(functions, variables, initial_values, xf, h)
    print(pontos)
    mostrar_grafico(pontos)

    output_file.write(str(pontos[-1][1])+"\n")

    input_file.close()
    output_file.close()

main()