import math  # Importa a biblioteca para usar fatorial

# Inicializa a soma
s = 0.0

# Calcula a série para 5 termos
for i in range(5):
    denominador = math.factorial(2 * i)  # Calcula (2i)!
    termo = i / denominador              # Calcula i / (2i)!
    s += termo                           # Soma ao total

print(f"O valor da série para 5 termos é: {round(s, 6)}")