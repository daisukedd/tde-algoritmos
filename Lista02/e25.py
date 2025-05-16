import math

# Entrada dos coeficientes
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

# Verificação se é equação do 2 grau
if a == 0:
    print("Não é equação de segundo grau.")
else:
    # Calcula o delta
    delta = b**2 - 4*a *c

    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Raiz única: {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Duas raízes reais: x1 = {x1:.2f}, x2 = {x2:.2f}")