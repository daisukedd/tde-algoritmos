# Variáveis para armazenar os resultados
soma = 0
quantidade = 0
maior_numero = float('-inf')
menor_numero = float('inf')
soma_pares = 0
quantidade_pares = 0

# Loop para leitura dos números
while True:
    numero = int(input("Digite um número (0 para finalizar): "))
    
    if numero == 0:
        break  # Encerra o laço se digitar 0
    
    soma += numero
    quantidade += 1

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1

# Cálculo das médias
media = soma / quantidade if quantidade > 0 else 0
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0

# Exibição dos resultados
print(f"\n(a) Soma dos números digitados: {soma}")
print(f"(b) Quantidade de números digitados: {quantidade}")
print(f"(c) Média dos números digitados: {media:.2f}")
print(f"(d) Maior número digitado: {maior_numero}")
print(f"(e) Menor número digitado: {menor_numero}")
print(f"(f) Média dos números pares: {media_pares:.2f}")