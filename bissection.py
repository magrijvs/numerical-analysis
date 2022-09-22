from math import e
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#f = input('Entre com a funcao f: ')
#f = e**x-2*x-1

a = int(input('Insira o valor a do intervalo [a,b]: '))

b = int(input('Insira o valor b do intervalo [a,b]: '))

tol = float(input('Entre com a precisao desejada: '))

kmax = int(input('Entre com o numero maximo de iteracoes: '))

k = 0

def f(x):
    return e**x-2*x-1

while (k < kmax):

    k = k + 1
    a
    b
    x = (a + b) / 2
    f(x)

    if ((b - a) < tol):
        print('A raiz eh: ', x)
        break

    if (f(a) * f(x) < 0):
        b = x;
    else:
        a = x;

    if (f(a) * f(x) == 0):
        print('A raiz eh: ', x)
        break

print('O numero de iteracoes para atingir a precisao desejada foi k= ', k);

x = np.linspace(a, b)
y = f(x)