a, b = 0, 1  # Início da sequência de Fibonacci
soma_pares = 0

# Enquanto o termo atual for até 4 milhões
while a <= 4000000:
    if a % 2 == 0:
        soma_pares += a
    a, b = b, a + b

# Exibe a soma dos termos pares
print(f"A soma dos termos pares da sequência de Fibonacci até 4 milhões é: {soma_pares}")