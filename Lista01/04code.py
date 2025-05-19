# Ler um número real e imprimir o quadrado desse número

while True:
    userInput = input("Digite um número real: ")

    try:
        numero = float(userInput)
        quadrado = numero ** 2  # Eleva o número ao quadrado
        print(f"Tipo do número: {type(numero)}")  #Valida que é float
        print(f"\n\U0001F389 O quadrado de {numero} é {quadrado} \U0001F389")
        break
    except ValueError: # Se não for possível converter para float
        print("\u274C Valor inválido. Digite um número real! \U0001F501")
