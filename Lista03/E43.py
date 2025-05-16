soma_idades = 0  # Armazena a soma das idades
quantidade = 0   # Conta quantas idades foram digitadas

# Laço infinito
while True:
    idade = int(input("Digite uma idade (0 para encerrar): "))
    
    # Se for 0, encerra
    if idade == 0:
        break

    soma_idades += idade
    quantidade += 1

# Verifica se houve entrada válida
if quantidade > 0:
    media = soma_idades / quantidade
    print(f"A idade média do grupo é: {media:.2f} anos.")
else:
    print("Nenhuma idade válida foi informada.")