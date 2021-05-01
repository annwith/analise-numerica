import numpy as np

def eliminacao_gauss(m):
    # percorre colunas
    for i in range(0, m.shape[0]-1):
        sub = m[i+1:, i] / m[i][i]
        print(sub)
        for j in range(i, m.shape[0]-1):
            m[j+1, :] = m[j+1, :] - sub[j-i]*m[i, :]
        print(m)

    res = []
    for i in range(m.shape[0]-1, -1, -1):
        res.append((m[i][-1] - np.sum(m[i, i+1:-1])) / m[i][i])
        m[:, i] *= res[-1]

    return res