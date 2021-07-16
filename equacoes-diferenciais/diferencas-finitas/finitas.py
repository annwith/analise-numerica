from utils import *
import numpy as np
import matplotlib.pyplot as plt

def eliminacao_gauss(m):
    for i in range(0, m.shape[0]-1):
        sub = m[i+1:, i] / m[i][i]
        for j in range(i, m.shape[0]-1):
            m[j+1, :] = m[j+1, :] - sub[j-i]*m[i, :]

    x = []
    for i in range(m.shape[0]-1, -1, -1):
        x.append((m[i][-1] - np.sum(m[i, i+1:-1])) / m[i][i])
        m[:, i] *= x[-1]

    return np.flip(x)

def finitas(xi, xf, yi, yf, h, functions):
    # constantes da matriz
    diagonal = solve_diferential_function(['h'], [h], functions[0])
    cf = solve_diferential_function(['h'], [h], functions[1])

    t = int((xf-xi)/h)-1
    
    m = np.zeros((t, t))
    y = np.zeros((t, 1))
    
    for i in range(t):
        y[i] = cf
    y[0] += yi
    y[-1] += yf

    m[0][0] = diagonal
    m[0][1] = -1
    m[-1][-1] = diagonal
    m[-1][-2] = -1
    for i in range(1, m.shape[0]-1):
        m[i][i] = diagonal
        m[i][i-1] = -1
        m[i][i+1] = -1

    m = np.concatenate((m, y), axis=1)
    # print(m)

    y = eliminacao_gauss(m)

    pontos = []
    pontos.append([xi, yi])
    xi += h
    for i in range(y.shape[0]):
        pontos.append([xi, y[i]])
        xi += h
    pontos.append([xi, yf])
    print(pontos)
    return np.asarray(pontos)

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
    initial_values = lines[1].split()
    final_values = lines[2].split()
    for i in range(len(initial_values)):
        initial_values[i] = float(initial_values[i])
    for i in range(len(final_values)):
        final_values[i] = float(final_values[i])
    h = float(lines[3].split()[0])

    xi = initial_values[0]
    xf = final_values[0]
    yi = initial_values[1]
    yf = final_values[1]

    pontos = finitas(xi, xf, yi, yf, h, functions)
    print(pontos)
    mostrar_grafico(pontos)

    output_file.write(str(pontos))

    input_file.close()
    output_file.close()

main()
