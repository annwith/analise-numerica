from utils import *
import math
import numpy as np
import matplotlib.pyplot as plt

# método de passo único direto
def ralston(funcao, x_i, x_f, y_i, h):
    pontos = []
    pontos.append([x_i, y_i])

    while(x_i < x_f):
        k1 = solve_dif_func(x_i, y_i, funcao)
        k2 = solve_dif_func(x_i+(3/4)*h, y_i+(3/4)*h*k1, funcao)
        y_i = y_i + (1/3*k1+2/3*k2)*h
        x_i += h
        pontos.append([x_i, y_i])

    return pontos

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
    for l in input_file:
        l = l.split()
        funcao = l[0]
        xi = float(l[1].split('=')[1])
        xf = float(l[2].split('=')[1])
        yi = float(l[3].split('=')[1])
        h = float(l[4].split('=')[1])
    
    pontos = ralston(funcao, xi, xf, yi, h)
    print(pontos)
    mostrar_grafico(pontos)

    output_file.write(str(pontos[-1][1])+"\n")

    input_file.close()
    output_file.close()

main()