clear
format long
x(1) = 1.8; % ponto(chute) inicial x0 de[a, b] = [1, 2]
epsilon = 0.5e-3; % tolerancia epsilon / numero de digitos(casas) decimais corretas
k = 0;
L = 2 / 3;

do
k + +;
x(k + 1) = log10(2 * x(k) + 1) / log10(e); % ln(2x_{k + 1} + 1)
until((abs(x(k + 1) - x(k)) / abs(x(k + 1))) <= epsilon)

x'

k0_calculando = (log10(abs(x(2) - x(1))) - log10(epsilon * (1 - L))) / (log10(1 / L)) + 1

k0 = floor(k0_calculando)

k

disp('k deve ser menor ou igual a k0. A precisao deve ser alcancada em no maximo k0 iteracoes')

% Substituindo qsi = x_{k + 1} em f: f(qsi) proximo de zero
function y = fun(x)
y = exp(x) - 2 * x - 1;
end

fqsi = fun(x(k + 1));