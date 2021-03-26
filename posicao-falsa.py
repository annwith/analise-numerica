import math

# Definir o número de casas de precisão pra fazer os cálculos
def posicao_falsa(funcao, a, b, precisao):
    # Inicialização
    iteracao = 0
    f_a = funcao(a)
    f_b = funcao(b)
    
    print(str(iteracao)+"\t"+str(a)+"\t"+str(b)+"\t"+str(f_a)+"\t"+str(f_b))
    
    repeat = False
    if (abs(f_a) > precisao and abs(f_b) > precisao):
        repeat = True

    # Loop
    while(repeat):
        iteracao += 1

        # Escolher 0 entre pontos a e b
        c = (a*f_b-b*f_a)/(f_b-f_a)
        f_c = funcao(c)

        if f_a*f_c < 0:
            b = c
            f_b = funcao(b)
        else:
            a = c
            f_a = funcao(a)

        print(str(iteracao)+"\t"+str(a)+"\t"+str(b)+"\t"+str(f_a)+"\t"+str(f_b))

        repeat = False
        if (abs(f_a) > precisao and abs(f_b) > precisao):
            repeat = True

def main():
    def funcao(x):
        return 0.25*(x-2)+0.1*math.sin(x)

    posicao_falsa(funcao, 1, 2, precisao=0.001)

main()