'''
Método dos Mínimos Quadrados
Erro: sum(ymedido - ymodelo)²
Minimizar o erro
'''
import numpy as np

'''
Input: Lista de pontos
Output: a0, a1 e o coeficiente de correlação
'''
def regressao_linear(pontos):
    p = np.asarray(pontos)
    x = p[:, 0]
    y = p[:, 1]

    n = p.shape[0]

    # Cálculo da reta
    a1 = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    a1 /= n*np.sum(x*x) - np.sum(x)**2
    a0 = np.average(y) - a1*np.average(x)

    # Coeficiente de correlação
    r = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    r /= (n*np.sum(x*x) - np.sum(x)**2)**(1/2)
    r /= (n*np.sum(y*y) - np.sum(y)**2)**(1/2)

    return a0, a1, r

# e pra quadratica como fica?
def potencia(pontos):
    p = np.asarray(pontos)
    p = np.log10(p)

    a0, a1, r = regressao_linear(p)

    log_a0 = np.log10(abs(a0))

    if a0 < 0:
        log_a0 *= -1
    
    print(log_a0)
    print(a1)
    print(r)

    # y = log_a0*x^a1
    return log_a0, a1, r

def exponencial(pontos):
    p = np.asarray(pontos)
    p[:, 1] = np.log(p[:, 1])

    a0, a1, r = regressao_linear(p)

    pass

def saturacao(pontos):
    pass

def predict(a0, a1, x):
    return a0+a1*x

p = [[1, 0.5],
    [2, 2.5],
    [3, 2.0],
    [4, 4.0],
    [5, 3.5],
    [6, 6.0],
    [7, 5.5]]

q = [[1, 0.5],
    [2, 1.7],
    [3, 3.4],
    [4, 5.7],
    [5, 8.4],
    ]

potencia(q)
