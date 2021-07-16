from utils import *
import math
import numpy as np
import matplotlib.pyplot as plt

def solve_system_ralston(functions, variables, values, x_f, h):
    pontos = []
    for value in values:
        pontos.append(value)
    
    # constantes
    k = np.zeros((4, len(variables)-1))
    
    while(values[0] < x_f):
        aux = []
        aux.append(values[0])
        # definir constantes
        for i in range(len(variables)-1):
            k[0][i] = h*solve_diferential_function(variables, values, functions[i])
        aux[0] = values[0]+h*(3/4)
        for j in range(len(variables)-1):
            aux.append(values[j+1]+k[0][j]*(3/4))
        for i in range(len(variables)-1):
            k[1][i] = h*solve_diferential_function(variables, aux, functions[i])
        
        for i in range(len(variables)-1):
            aux[i+1] = values[i+1] + ((1/3)*k[0][i]+(2/3)*k[1][i])
        aux[0] = values[0]+h

        # só atualiza os valores juntos
        for i in range(len(aux)):
            values[i] = aux[i]
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
    y_grafico = int(lines[5].split()[0])

    pontos = solve_system_ralston(functions, variables, initial_values, xf, h)
    print(pontos)
    x = pontos[:, 0]
    y = pontos[:, y_grafico]
    grafico = np.concatenate((x, y))
    grafico = np.reshape(grafico, (x.shape[0], 2), order='F')
    mostrar_grafico(grafico)

    for i in range(len(variables)):
        output_file.write(variables[i]+": "+str(pontos[-1][i])+"\n")

    input_file.close()
    output_file.close()

main()