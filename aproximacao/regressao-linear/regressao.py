'''
Método dos Mínimos Quadrados
Erro: sum(ymedido - ymodelo)²
Minimizar o erro
'''
import numpy as np
import matplotlib.pyplot as plt

'''
Input: Lista de pontos
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

def exponencial(pontos):
    pontos = np.asarray(pontos)
    pontos[:, 1] = np.log(pontos[:, 1])

    a0, a1, r = regressao_linear(pontos)

    pass

def saturacao(pontos):
    pass

# tem que ter uma predição pra potencia tbm?
def predicao(a0, a1, x, potencia):
    if potencia:
        return 10**(a0 + a1*np.log10(x)) # log 
    return a0 + a1*x

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
    for l in input_file:
        if l == "potencia\n":
            potencia = True
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
        y = predicao(a0, a1, x, potencia)
        output_file.write(str(y))
    else:
        pontos = np.asarray(pontos)
        if potencia:
            print("Potencia!")
            pontos = np.log10(pontos)
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