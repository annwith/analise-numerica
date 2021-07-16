from utils import solve_dif_func
import math
import numpy as np
import matplotlib.pyplot as plt

# método de passo único direto
def runge(funcao, x_i, x_f, y_i, h):
    pontos = []
    pontos.append([x_i, y_i])

    while(x_i < x_f):
        # print(x_i)
        k1 = solve_dif_func(x_i, y_i, funcao)
        k2 = solve_dif_func(x_i+(1/2)*h, y_i+(1/2)*h*k1, funcao)
        k3 = solve_dif_func(x_i+(1/2)*h, y_i+(1/2)*h*k2, funcao)
        k4 = solve_dif_func(x_i+h, y_i+h*k3, funcao)
        y_i = y_i + (1/6)*(k1+2*k2+2*k3+k4)*h
        x_i += h
        pontos.append([x_i, y_i])

    return pontos

def grade_adaptativa(funcao, x_i, x_f, y_i, h, dif_y):
    pontos = []
    pontos.append([x_i, y_i])

    while(x_i < x_f):
        y_i = pontos[-1][1] 
        h_i = h
        p = runge(funcao, x_i, x_i+h, y_i, h)
        y_ant = p[-1][1]
        h_i = h_i/2
        p = runge(funcao, x_i, x_i+h, y_i, h_i)
        y_f = p[-1][1]
        print(y_ant)
        print(y_f)
        print(y_ant-y_f)

        while(abs(y_ant-y_f)>dif_y):
            y_ant = y_f
            print(y_ant-y_f)
            print(h_i)
            h_i = h_i/2
            p = runge(funcao, x_i, x_i+h, y_i, h_i)
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


funcao2 = "4*E^(0.8*x)-0.5*y"
funcao1 = "-2*x^3+12*x^2-20*x+8.5"
funcao3 = "(2000-2*y)/(200-x)"

p = grade_adaptativa(funcao3, 0, 50, 0, 1, 0.1)
mostrar_grafico(p)
print(p)

f1 = ["4*E^(0.8*x)-0.5*y"]