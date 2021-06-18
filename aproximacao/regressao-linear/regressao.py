'''
Método dos Mínimos Quadrados
Erro: sum(ymedido - ymodelo)²
Minimizar o erro
'''
import numpy as np
import matplotlib.pyplot as plt
import math

'''
Input: NumPy array de pontos
Output: a0, a1 e o coeficiente de correlação
'''
def regressao_linear(pontos):
    x = pontos[:, 0]
    y = pontos[:, 1]

    n = pontos.shape[0]

    # Cálculo da reta
    a1 = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    a1 /= n*np.sum(x*x) - np.sum(x)**2
    a0 = np.average(y) - a1*np.average(x)

    # Coeficiente de correlação
    r = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    r /= (n*np.sum(x*x) - np.sum(x)**2)**(1/2)
    r /= (n*np.sum(y*y) - np.sum(y)**2)**(1/2)

    return a0, a1, r

'''
Input: Coeficiente linear, coeficiente angular, x, potencia(True or False)
Output: f(x)
'''
def predicao(a0, a1, x, potencia, exponencial, saturacao):
    if potencia:
        return 10**(a0 + a1*np.log10(x)) 
    if exponencial:
        return math.e**(a0+a1*x) 
    if saturacao:
        return 1/(a0 + a1*(1/x)) 
    return a0 + a1*x

'''
Input: NumPy array de pontos, coef. linear e coef. angular
Output: Gráfico com os pontos e a reta
'''
def mostrar_grafico(pontos, a0, a1):
    # Data for plotting
    x = pontos[:, 0]
    y = pontos[:, 1]

    # Data for plotting
    xl = np.array((x[0], x[-1]))
    yl = a0 + xl*a1

    fig, ax = plt.subplots()
    ax.plot(x, y, 'o')
    ax.plot(xl, yl)

    ax.set(xlabel='x', ylabel='y')
    ax.grid()

    fig.savefig("regressao.png")
    plt.show()

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    pontos = []
    predict = False
    potencia = False
    exponencial = False
    saturacao = False
    for l in input_file:
        if l == "potencia\n":
            potencia = True
        elif l == "exponencial\n":
            exponencial = True
        elif l == "saturacao\n":
            saturacao = True
        else:
            l = l.split()
            l = [float(i) for i in l]
            if len(l) == 3:
                a0 = l[0] 
                a1 = l[1]
                x = l[2]
                predict = True
            elif len(l) == 2:
                pontos.append(l)
    
    if predict:
        y = predicao(a0, a1, x, potencia, exponencial, saturacao)
        output_file.write(str(y))
    else:
        pontos = np.asarray(pontos)
        if potencia:
            pontos = np.log10(pontos)
            a0, a1, r = regressao_linear(pontos)
        if exponencial:
            pontos[:, 1] = np.log(pontos[:, 1])
            a0, a1, r = regressao_linear(pontos)
        if saturacao:
            pontos = 1/pontos
            a0, a1, r = regressao_linear(pontos)
        else:
            a0, a1, r = regressao_linear(pontos)

        output_file.write("a0 = "+str(a0)+"\n")
        output_file.write("a1 = "+str(a1)+"\n")
        output_file.write("r = "+str(r)+"\n")

        mostrar_grafico(pontos, a0, a1)
    
    input_file.close()
    output_file.close()

main()