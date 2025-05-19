# Ler e Imprimir um número inteiro (com repetição até valor válido)

while True:
    userInput = input("Digite um número inteiro: ")

    if userInput.isdigit(): #Validação
        number = int(userInput)
        print(f"\U0001F389 O número digitado foi: {number} \U0001F389")
        print(f"Tipo do número: {type(number)}")      # Input convertido para inteiro
        print(f"Tipo do input: {type(userInput)}")    # Input ainda é string
        break
    else:
        print("\U0001F501 Input inválido. Insira um número inteiro! \U0001F501")
