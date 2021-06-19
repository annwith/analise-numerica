from utils import solve_func

def derivada(funcao, x, h):
    derivada_primeira = (solve_func(x+h, funcao)-solve_func(x-h, funcao))/(2*h)
    derivada_segunda = (solve_func(x+h, funcao)-2*solve_func(x, funcao)+solve_func(x-h, funcao))/(h**2)
    return derivada_primeira,derivada_segunda

def main():
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    for l in input_file:
        l = l.split()
        funcao = l[0]
        x = float(l[1])
        h = float(l[2])
    
    d1, d2 = derivada(funcao, x, h)

    output_file.write(str(d1)+"\n")
    output_file.write(str(d2))

    input_file.close()
    output_file.close()

main()