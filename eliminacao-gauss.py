import numpy as np

def eliminacao_gauss(m):
    # percorre colunas
    for i in range(0, m.shape[0]-1):
        sub = m[i+1:, i] / m[i][i]
        # print(sub)
        for j in range(i, 2):
            m[j+1, :] = m[j+1, :] - sub[j-i]*m[i, :]
        # print(m)

    res = []
    for i in range(m.shape[0]-1, -1, -1):
        res.append((m[i][-1] - np.sum(m[i, i+1:-1])) / m[i][i])
        m[:, i] *= res[-1]

    return res
    
m = [[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]]
m2 = [[0, 7, -0.3, -19.3], [0.3, 0, 10, 71.4], [3, -0.1, -0.2, 7.85]]
m = np.asarray(m)
m2 = np.asarray(m2)
# pivotamento(m2)
# print(m2)
res = eliminacao_gauss(m)
print(res)