'''
Método dos Mínimos Quadrados
Erro: sum(ymedido - ymodelo)²
Minimizar o erro
'''
import numpy as np

'''
Input: Lista de pontos
Output: a1 e a0
'''
def regressao_linear(p):
    p = np.asarray(p)
    # print(p)
    # print(p.shape)
    x = p[:, 0]
    y = p[:, 1]
    log_x = np.log10(x)
    log_y = np.log10(y)
    print(log_x)
    print(log_y)
    n = p.shape[0]
    # print(x*y)
    def line(x, y):
        # Cálculo da reta
        a1 = n*np.sum(x*y) - np.sum(x)*np.sum(y)
        a1 /= n*np.sum(x*x) - np.sum(x)**2
        a0 = np.average(y) - a1*np.average(x)

        # Coeficiente de correlação
        r = n*np.sum(x*y) - np.sum(x)*np.sum(y)
        r /= (n*np.sum(x*x) - np.sum(x)**2)**(1/2)
        r /= (n*np.sum(y*y) - np.sum(y)**2)**(1/2)
        
        return a1, a0, r

    # reta
    a1, a0, r = line(x, y)
    print(a1)
    print(a0)
    print(r)

    # potencia
    a1, a0, r = line(log_x, log_y)
    print(a1)
    print(a0)
    print(r)

    # saturação

    # exponencial

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

regressao_linear(q)