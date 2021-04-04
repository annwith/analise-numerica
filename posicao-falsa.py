import math

# Definir o número de casas de precisão pra fazer os cálculos
def posicao_falsa(funcao, a, b, precisao):
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
    
    it.append([iteracao, a, b, f_a, f_b])
    
    repeat = False
    if (abs(f_a) > precisao and abs(f_b) > precisao):
        repeat = True

    # Loop
    while(repeat and a < b):
        iteracao += 1

        # Escolher 0 entre pontos a e b
        # f_b - f_a != 0 (TRATAR ISSO)
        c = (a*f_b-b*f_a)/(f_b-f_a)
        f_c = funcao(c)

        if f_a*f_c < 0:
            b = c
            f_b = funcao(b)
        else:
            a = c
            f_a = funcao(a)

        it.append([iteracao, a, b, f_a, f_b])

        repeat = False
        if (abs(f_a) > precisao and abs(f_b) > precisao):
            repeat = True
    
    return it