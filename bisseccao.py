import math

# Definir o número de casas de precisão pra fazer os cálculos
def bisseccao(funcao, a, b, precisao_a=None, precisao_b=None, precisao_absoluta=None, precisao_relativa=None):
    # Inicialização
    iteracao = 0
    f_a = funcao(a)
    f_b = funcao(b)
    d_absoluta = abs(a-b)
    d_relativa = abs((a-b)/a)
    
    print(str(iteracao)+"\t"+str(a)+"\t"+str(b)+"\t"+str(f_a)+"\t"+str(f_b)+"\t"+str(d_absoluta)+"\t"+str(d_relativa))
    
    repeat = False
    if (precisao_absoluta != None and d_absoluta > precisao_absoluta):
        repeat = True
    if (precisao_relativa != None and d_relativa > precisao_relativa):
        repeat = True
    if (precisao_a != None and abs(f_a) > precisao_a):
        repeat = True
    if (precisao_b != None and abs(f_b) > precisao_b):
        repeat = True

    # Loop
    while(repeat):
        iteracao += 1

        # Escolher uma metade
        meio = (a+b)/2
        f_meio = funcao(meio)

        if f_a*f_meio < 0:
            b = meio
            f_b = funcao(b)
        else:
            a = meio
            f_a = funcao(a)
        
        d_absoluta = abs(a-b)
        d_relativa = abs((a-b)/a)

        print(str(iteracao)+"\t"+str(a)+"\t"+str(b)+"\t"+str(f_a)+"\t"+str(f_b)+"\t"+str(d_absoluta)+"\t"+str(d_relativa))

        repeat = False
        if (precisao_absoluta != None and d_absoluta > precisao_absoluta):
            repeat = True
        if (precisao_relativa != None and d_relativa > precisao_relativa):
            repeat = True
        if (precisao_a != None and abs(f_a) > precisao_a):
            repeat = True
        if (precisao_b != None and abs(f_b) > precisao_b):
            repeat = True

# Definir o número de iterações necessárias
def iteracoes_bisseccao(a, b, precisao_absoluta):
    i = abs(a-b)
    n = (math.log(i)-math.log(precisao_absoluta))/math.log(2)
    return n

def main():
    def funcao(x):
        return 0.25*(x-2)+0.1*math.sin(x)

    bisseccao(funcao, 1, 2, precisao_absoluta=0.001)

    iteracoes = iteracoes_bisseccao(1, 2, precisao_absoluta=0.001)
    print(math.ceil(iteracoes))

main()