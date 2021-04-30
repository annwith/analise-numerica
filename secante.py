import math

def secante(funcao, a, b, precisao):
    # se a maior que b: trocar
    if a > b:
        [a, b] = [b, a]

    iteracao = 0
    f_a = funcao(a)
    f_b = funcao(b)
    it = []

    it.append([a, f_a])
    it.append([b, f_b])

    # Limite de vezes seguidas que a(k)-a(k-1) > a(k-1)-a(k-2)
    limite = 0

    # Inicialização
    f_x_2 = f_a
    while(abs(f_x_2) > precisao):
        iteracao += 1

        # Atualização do ponto de acordo com a funcao de convergencia
        x_1 = it[-1][0]
        f_x_1 = it[-1][1]
        x_0 = it[-2][0]
        f_x_0 = it[-2][1]
        x_2 = (f_x_1*x_0 - f_x_0*x_1) / (f_x_1 - f_x_0)
        f_x_2 = funcao(x_2)
        it.append([x_2, f_x_2])

        # Verificar se está convergindo
        d_anterior = abs(it[iteracao-2][0]-it[iteracao-1][0])
        d_atual = abs(it[iteracao-1][0]-it[iteracao][0])

        if d_anterior < d_atual:
            limite += 1
        else:
            limite = 0
            
        if limite == 4:
            break
    
    return it

def funcao(x):
    return x**2+x-6

it = secante(funcao, 1.5, 2.5, 0.001)
print(it)