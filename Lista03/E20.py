# Inicializa os contadores
total_lidos = 0
quantidade_pares = 0

# Loop de repetição até que o número 1000 seja digitado
while True:
    numero = int(input("Digite um número inteiro (1000 para sair): "))
    
    if numero == 1000:
        break  # Encerra o loop se o número for 1000
    
    total_lidos += 1  # Conta o número de entradas

    if numero % 2 == 0:
        quantidade_pares += 1  # Conta se o número for par

# Exibe a quantidade total de números lidos e quantos eram pares
print("Quantidade de números lidos:", total_lidos)
print("Quantidade de números pares:", quantidade_pares)