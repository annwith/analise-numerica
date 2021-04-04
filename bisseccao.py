import math

# Definir se existe 0 em um intervalo
def intervalo_zero(funcao, a, b):
    if funcao(a) * funcao(b) < 0:
        return True
    return False

# Definir o número de casas de precisão pra fazer os cálculos
def bisseccao(funcao, a, b, precisao=None, distancia_absoluta=None, distancia_relativa=None):
    # Garantir a < b e a != b
    if a > b:
        [a, b] = [b, a]
    elif a == b:
        return "Interval Error"

    # Inicialização
    it = []

    iteracao = 0
    f_a = funcao(a)
    f_b = funcao(b)
    d_absoluta = abs(a-b)
    if a != 0:
        d_relativa = abs((a-b)/a)
    else:
        d_relativa = None
    
    it.append([iteracao, a, b, f_a, f_b, d_absoluta, d_relativa])
    
    repeat = False
    if (distancia_absoluta != None and d_absoluta > distancia_absoluta):
        repeat = True
    if (a != 0 and distancia_relativa != None and d_relativa > distancia_relativa):
        repeat = True
    if (precisao != None and abs(f_a) > precisao and abs(f_b) > precisao):
        repeat = True

    # Loop
    while(repeat and a < b):
        iteracao += 1

        # Escolher uma metade
        c = (a+b)/2
        f_c = funcao(c)

        if f_a*f_c < 0:
            b = c
            f_b = funcao(b)
        else:
            a = c
            f_a = funcao(a)
        
        d_absoluta = abs(a-b)
        if a != 0:
            d_relativa = abs((a-b)/a)
        else:
            d_relativa = None

        it.append([iteracao, a, b, f_a, f_b, d_absoluta, d_relativa])

        repeat = False
        if (distancia_absoluta != None and d_absoluta > distancia_absoluta):
            repeat = True
        if (a != 0 and distancia_relativa != None and d_relativa > distancia_relativa):
            repeat = True
        if (precisao != None and abs(f_c) > precisao):
            repeat = True
    
    return it

# Definir o número de iterações necessárias
def iteracoes_bisseccao(a, b, distancia_absoluta):
    i = abs(a-b)
    n = (math.log(i)-math.log(distancia_absoluta))/math.log(2)
    return n