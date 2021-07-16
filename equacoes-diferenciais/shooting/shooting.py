from utils import *
import math
import numpy as np
import matplotlib.pyplot as plt

# aqui tem que ser de segunda ordem
def shooting(functions, variables, values_1, values_2, x_f, y_f, h):
    p1 = solve_system(functions, variables, values_1, 10, 1)
    p2 = solve_system(functions, variables, values_2, 10, 1)

    # O y tem que estar na segunda posição na lista
    y1 = p1[-1][1]
    y2 = p2[-1][1]
    print(y1)
    print(y2)

    z1 = p1[0][2]
    z2 = p2[0][2]
    print(z1)
    print(z2)

    # Regra de 3
    z0 = ((z2-z1)/(y2-y1))*(y_f-y1) + z1

    return z0

# resolve um sistema de equações com euler  
def solve_system(functions, variables, values, x_f, h):
    pontos = []
    pontos.append([values[0], values[1], values[2]])
    
    while(values[0] < x_f):
        i = 1
        for func in functions:
            # euler method
            values[i] += solve_diferential_function(variables, values, func)*h
            i += 1
        values[0] += h
        pontos.append([values[0], values[1], values[2]])

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

    fig.savefig("runge.png")
    plt.show()

functions = ["z", "-0.01*(20-y)"]
variables = ['x', 'y', 'z']
initial_values1 = [0, 40, 10]
initial_values2 = [0, 40, 20]

p = shooting(functions, variables, initial_values1, initial_values2, 10, 200, 1)
p = np.asarray(p)
print(p)