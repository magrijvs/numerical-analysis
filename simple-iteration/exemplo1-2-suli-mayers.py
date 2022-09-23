import math
from math import e

f= lambda x: x**6 -x -1

x(1) = 1.8; # valor(chute) inicial
tol = 0.5e-10; # precisao requerida
k = 0; # iteracoes(quantidade de elementos da sequencia)


do
k ++
x(k + 1) = math.log(2 * x(k) + 1),10) / math.log(e,10) # sequencia gerada pela iteracao g(x_k) = ln(2 x_{k} + 1)
until((abs(x(k + 1) - x(k)) / abs(x(k + 1))) <= tol) # criterio de parada pelo erro relativo

print(k) # imprime o numero de iteracoes x'               % imprime os elementos da sequencia
qsi = x(k + 1) % imprime a raiz aproximada, qsi, para f(x) = ex - 2x - 1

function y = fun(x)
    y = exp(x) - 2 * x - 1;
end

f_qsi = fun(x(k + 1)) # imprime o valor de f em qsi: f(qsi)

f1 = fun(1);
f2 = fun(2);
fqsiOCTAVE = fun(fzero("fun", [1 2]));