clear
format long
x(1) = 1.8; % valor(chute) inicial
tol = 0.5e-10; % precisao requerida
k = 0; % iteracoes(quantidade de elementos da sequencia)


do k + +;
x(k + 1) = log10(2 * x(k) + 1) / log10(e); % sequencia gerada pela iteracao g(x_k) = ln(2 x_{k} + 1)
until((abs(x(k + 1) - x(k)) / abs(x(k + 1))) <= tol) % criterio de parada pelo erro relativo

k % imprime o numero de iteracoes x'               % imprime os elementos da sequencia
qsi = x(k + 1) % imprime a raiz aproximada, qsi, para f(x) = ex - 2x - 1

function y = fun(x)
    y = exp(x) - 2 * x - 1;
end

f_qsi = fun(x(k + 1)) % imprime o valor de f em qsi: f(qsi)