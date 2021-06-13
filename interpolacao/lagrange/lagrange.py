import numpy as np

# quando adiciona um ponto tem que fazer tudo de novo
def lagrange(pontos):
    x = pontos[:, 0]
    y = pontos[:, 1]
    n = len(x) # numero de pontos

    print(x)
    print(y)

    l = np.zeros((n, n-1, 2), dtype=np.float64)
    divisor = np.ones((n), dtype=np.float64)

    # Todos os agrupamentos de x-1 possível (x agrupamentos)
    for i in range(n):
        ind = 0
        for j in range(n):
            if i != j:
                # (x-1)(x-5)(x-6)
                l[i][ind][0] = -x[j]  # grau 0
                l[i][ind][1] = 1        # grau 1
                divisor[i] *= x[i]-x[j]
                ind += 1

    print(l)
    print(divisor)

    # Multiplica dois polinomios
    # A posição em p1 e p2 indica o grau e o valor o coeficiente: [-6, 1] = x-6
    def mul(p1, p2):
        grau_max = p1.shape[0]+p2.shape[0]-1
        p = np.zeros((grau_max)) # grau maximo do polinomio resultante
        for i in range(p1.shape[0]):
            for j in range(p2.shape[0]):
                grau = i+j # descobrir o grau
                p[grau] += p1[i]*p2[j] # multiplicar coeficientes
        return p

    p = []
    for i in range(n):
        p.append(l[i][0])

    for i in range(n):
        for j in range(1, l.shape[1]):
            p[i] = mul(p[i], l[i][j])
    
    p = np.asarray(p)
    print(p)

    # dividindo os polinomios pelo valor que eles devem ser divididos
    for i in range(n):
        p[i] /= divisor[i]
        # p[i] *= y[i]

    print(p)

    # multiplicando os polinomios por y
    for i in range(n):
        p[i] *= y[i]

    print(p)

    # fazendo a soma
    p = np.sum(p, axis=0)
    print(p)

    return p

pontos = [[1, np.log(1)], [4, np.log(4)], [6, np.log(6)], [5, np.log(5)]]
pontos = np.asarray(pontos)

lagrange(pontos)
