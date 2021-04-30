# Definir se existe 0 em um intervalo
def intervalo_zero(funcao, a, b):
    if funcao(a) * funcao(b) < 0:
        return True
    return False

# Tirar 0 da diagonal
def pivotamento(m):
    for i in range(0, m.shape[0]):
        if m[i][i] == 0: # qual precisão considera 0?
            for j in range(0, m.shape[0]):
                if m[j][i] != 0: # qual precisão considera 0?
                    # trocar linhas do array
                    m[[i, j]] = m[[j, i]]