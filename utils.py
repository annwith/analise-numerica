from func_input import func_parser 

# Resolver uma função
def solve_func(x, func):
    func = func.replace('x', str(x))
    return func_parser(func)

# Definir se existe 0 em um intervalo
def intervalo_zero(funcao, a, b):
    if funcao(a) * funcao(b) < 0:
        return True
    return False

# Tirar 0 da diagonal - Evitar divisão por 0
def zeros_diagonal(m):
    for i in range(0, m.shape[0]):
        if m[i][i] == 0: # qual precisão considera 0?
            for j in range(0, m.shape[0]):
                if m[j][i] != 0: # qual precisão considera 0?
                    # trocar linhas do array
                    m[[i, j]] = m[[j, i]]

# Colocar os maiores valores possíveis na diagonal
# Pivoteamento

# Calculo do determinante

# Teste do resultado final da matriz