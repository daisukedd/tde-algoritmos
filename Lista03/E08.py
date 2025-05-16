# Encontra o menor e o maior número entre 10 valores

numeros = []

for i in range(10):                  # Loop para 10 entradas
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

menor = min(numeros)                 # Encontra menor
maior = max(numeros)                 # Encontra maior

print(f"Menor valor lido: {menor}")
print(f"Maior valor lido: {maior}")