import numpy as np

def fatoracao_lu(m, lub=False):
    # Inicializar matriz LU e b
    if lub == False:
        # Construir matriz LU
        lu = np.zeros_like(m[:, :-1])

        i = 0
        lu[i, :] = m[i, :-1]
        lu[i+1:, i] = m[i+1:, i] / m[i][i]

        for i in range(1, m.shape[0]):
            # coluna l
            for j in range(0, i):
                lu[i][j] = (m[i][j] - np.sum(lu[i, :j]*lu[:j, j])) / lu[j][j]
            # linha u
            for j in range(i, m.shape[0]):
                lu[i][j] = m[i][j] - np.sum(lu[i, :i]*lu[:i, j])
    else:
        lu = m[:, :-1]
    
    b = m[:, -1]

    # Ly = b : substituição direta
    y = []
    l = lu
    for i in range(l.shape[0]):
        y.append((b[i] - np.sum(l[i, :i])) / 1)
        l[i+1:, i] *= y[-1]
        # print(l)

    x = []
    # Ux = y substituição reversa
    for i in range(m.shape[0]-1, -1, -1):
        x.append((y[i] - np.sum(l[i, i+1:])) / l[i][i])
        l[:i, i] *= x[-1]
        # print(l)

    return lu, x