# Ler e imprimir um número real com repetição até valor válido

while True:
    userInput = input("Digite um número real: ")

    # Validação: tenta converter para float verificando se é um número real
    if userInput.replace('.', '', 1).replace('-', '', 1).isdigit(): # Valida manual / Remover ponto e sinal negativo
        
        number = float(userInput) # Converte para float
        print(f"\U0001F389 O número digitado foi: {number} \U0001F389")
        print(f"Tipo do número: {type(number)}")      # Input convertido para float
        print(f"Tipo do input: {type(userInput)}")    # Input ainda é string
        break
    else:
        print("\U0001F501 Input inválido. Insira um número real! \U0001F501")
