primeiro = True  # Indica se é o primeiro número digitado

# Laço até que o usuário digite um número negativo
while True:
    num = int(input("Digite um número inteiro (negativo para sair): "))
    
    if num < 0:
        break

    if primeiro:
        maior = menor = num  # Inicializa maior e menor com o primeiro valor
        primeiro = False
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

# Exibe os resultados ou mensagem de erro caso nenhum número tenha sido digitado
if primeiro:
    print("Nenhum número válido foi digitado.")
else:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")