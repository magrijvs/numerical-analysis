import numpy as np
from math import e

formulaInput = input('Entre com a funcao f: ')
a = int(input('Digite um valor inicial para o intervalo: '))
b = int(input('Digite um valor final para o intervalo: '))
ATOL = float(input('Entre com a precisao desejada: '))

n = np.ceil(np.log2((a + b) / (2 * ATOL)))
a_alg = a
b_alg = b

def formula(x):
    return eval(formulaInput)

for i in range(int(n)):
    x = (a_alg + b_alg) / 2
    f_x = formula(x)

    if formula(a_alg) * f_x < 0:
        b_alg = x
    else:
        a_alg = x

print("Número de iterações:", int(n))
print("Erro absoluto da resposta:", np.abs(np.pi - x))
print("x encontrado:", x)
print("x esperado:", np.pi)
print("Erro de f(x)", np.abs(np.sin(x)))