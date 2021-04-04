import math

def ponto_fixo(funcao, f_conv, a, precisao):
    iteracao = 0
    f_a = funcao(a)
    it = []

    it.append([a, f_a])

    # Limite de vezes seguidas que a(k)-a(k-1) > a(k-1)-a(k-2)
    limite = 0

    while(abs(f_a) > precisao):
        iteracao += 1

        # Atualização do ponto de acordo com a funcao de convergencia
        a = f_conv(a)
        f_a = funcao(a)
        it.append([a, f_a])

        if iteracao > 1:
            d_anterior = abs(it[iteracao-2][0]-it[iteracao-1][0])
            d_atual = abs(it[iteracao-1][0]-it[iteracao][0])

            if d_anterior < d_atual:
                limite += 1
            else:
                limite = 0
            
        if limite == 4:
            break
    
    return it