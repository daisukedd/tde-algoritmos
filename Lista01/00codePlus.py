def derivada(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def f(x):
    return x**2


x = float(input("Digite o valor de x para calcular a derivada de f(x) = x^2: "))
d = derivada(f, x)

print(f"A derivada aproximada de f(x) no ponto x = {x} é {d:.5f}")
