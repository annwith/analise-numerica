from utils import solve_dif_func
import math

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
    
    pontos = euler(funcao, xi, xf, yi, h)
    mostrar_grafico(pontos)

    output_file.write(str(pontos[-1][y])+"\n")

    input_file.close()
    output_file.close()

main()