# Fazer pivoteamento
# Verificar se a matriz está mal condicionada
import numpy as np

def eliminacao_gauss(m):
    # percorre colunas
    for i in range(0, 2):
        sub = m[i+1:, i] / m[i][i]
        # print(sub)
        for j in range(i, 2):
            m[j+1, :] = m[j+1, :] - sub[j-i]*m[i, :]
        # print(m)

    res = []
    for i in range(2, -1, -1):
        res.append((m[i][-1] - np.sum(m[i, i+1:-1])) / m[i][i])
        m[:, i] *= res[-1]
        # print(m)
        # print(res)
    
m = [[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]]
m = np.asarray(m)
eliminacao_gauss(m)