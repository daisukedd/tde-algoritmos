limite = 2_000_000  # Limite para o cálculo

# Inicializa a lista marcando todos os números como primos
primos = [True] * limite
primos[0] = primos[1] = False  # 0 e 1 não são primos

# Crivo de Eratóstenes para marcar os não primos
for i in range(2, int(limite ** 0.5) + 1):
    if primos[i]:
        for j in range(i*i, limite, i):
            primos[j] = False

# Soma os índices marcados como primos
soma_primos = sum(i for i, eh_primo in enumerate(primos) if eh_primo)

print(f"A soma de todos os números primos abaixo de dois milhões é: {soma_primos}")