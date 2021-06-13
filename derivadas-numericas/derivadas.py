import numpy as np
from utils import solve_func

def derivada(funcao, x, h):
    derivada_centrada_primeira = (solve_func(x+h, funcao)-solve_func(x-h, funcao))/(2*h)
    derivada_centrada_segunda = (solve_func(x+h, funcao)-2*(solve_func(x, funcao)+(solve_func(x-h, funcao))/(h**2)
    return derivada_centrada_primeira, derivada_centrada_segunda

func = 
primeira(func, 0.1)