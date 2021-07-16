from utils import *
import math
import numpy as np
import matplotlib.pyplot as plt

# aqui tem que ser de segunda ordem
def shooting(functions, variables, values_1, values_2, xf, y_f, h):
    xi = values_1[0] 
    yi = values_1[1]

    p1 = solve_system_runge(functions, variables, values_1, xf, h)
    p2 = solve_system_runge(functions, variables, values_2, xf, h)

    # O y tem que estar na segunda posição na lista
    y1 = p1[-1][1]
    y2 = p2[-1][1]

    z1 = p1[0][2]
    z2 = p2[0][2]

    # Regra de 3
    zi = ((z2-z1)/(y2-y1))*(y_f-y1) + z1

    pontos = solve_system_runge(functions, variables, [xi, yi, zi], xf, h)
    return pontos

def solve_system_runge(functions, variables, values, x_f, h):
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
        aux[0] = values[0]+h/2
        for j in range(len(variables)-1):
            aux.append(values[j+1]+k[0][j]/2)
        for i in range(len(variables)-1):
            k[1][i] = h*solve_diferential_function(variables, aux, functions[i])
        for j in range(len(variables)-1):
            aux[j+1] = values[j+1]+k[1][j]/2
        for i in range(len(variables)-1):
            k[2][i] = h*solve_diferential_function(variables, aux, functions[i])
        aux[0] = values[0]+h
        for j in range(len(variables)-1):
            aux[j+1] = values[j+1]+k[2][j]
        for i in range(len(variables)-1):
            k[3][i] = h*solve_diferential_function(variables, aux, functions[i])
        
        for i in range(len(variables)-1):
            aux[i+1] = values[i+1] + (k[0][i]+2*k[1][i]+2*k[2][i]+k[3][i])/6

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
    initial_values1 = lines[2].split()
    for i in range(len(initial_values1)):
        initial_values1[i] = float(initial_values1[i])
    initial_values2 = lines[3].split()
    for i in range(len(initial_values2)):
        initial_values2[i] = float(initial_values2[i])
    xf = float(lines[4].split()[0])
    yf = float(lines[5].split()[0])
    h = float(lines[6].split()[0])

    pontos = shooting(functions, variables, initial_values1, initial_values2, xf, yf, h)
    print(pontos)
    x = pontos[:, 0]
    y = pontos[:, 1]
    grafico = np.concatenate((x, y))
    grafico = np.reshape(grafico, (x.shape[0], 2), order='F')
    mostrar_grafico(grafico)

    output_file.write(str(pontos))

    input_file.close()
    output_file.close()

main()