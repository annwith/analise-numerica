import numpy as np
import math

# TAMANHO MÍNIMO DO SISTEMA: 2 EQUAÇÕES
def jacobi(m, var_absoluta=0.00001):
    x1 = np.zeros_like(m[:, :-1])
    np.fill_diagonal(x1, 0)
    d1 = math.inf
    #print(x1)
    a = m[:, :-1]
    b = m[:, -1]
    #print(a)
    #print(b)
    parada = 0
    i = 0
    while True:
        i += 1
        #print(np.sum(a*x1, axis=1))
        x2 = (b-np.sum(a*x1, axis=1))/np.diagonal(m)
        x2 = np.repeat(np.reshape(x2, (1, x2.shape[0])), [x2.shape[0]], axis=0)
        np.fill_diagonal(x2, 0)
        d2 = np.absolute(x2-x1)
        # Variação absoluta
        if np.all(d2 < var_absoluta):
            x1 = np.copy(x2)
            break
        if np.sum(d2) > np.sum(d1):
            parada += 1
        else:
            parada = 0
        if parada == 4:
            return np.array([])
        x1 = np.copy(x2)
        d1 = d2

    x = x1[0, :]
    x[0] = x1[1][0]

    return x, i

def main():
    input_txt = open('input-jacobi.txt', 'r')
    output_txt = open('output-jacobi.txt', 'w')
    np.set_printoptions(precision=6)
    np.set_printoptions(suppress=True)

    m = []
    for line in input_txt:
        if line[-1] == '\n':
            line = line[:-1]
        if 'variacao_absoluta=' in line:
            var_absoluta = float(line.split('=')[1])
            break
        m.append(line.split(" "))
        m[-1] = list(map(lambda x: float(x), m[-1]))

    m = np.asarray(m)
    x, i = jacobi(np.copy(m), var_absoluta)
    output_txt.write("Iterações realizadas: "+str(i)+"\n")
    output_txt.write(str(x)+"\n")

    if x.shape[0] != 0:
        m[:, :-1] *= x
        n = np.sum(m[:, :-1], axis=1)
        n = np.abs(m[:,-1]-n)

        output_txt.write(str(n)+"\n")

    input_txt.close()
    output_txt.close()

main()