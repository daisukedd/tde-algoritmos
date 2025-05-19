# Ler um número real e imprimir a quinta parte desse número
# A quinta parte de um número é o valor dele dividido por 5

while True:
    userInput = input("Digite um número real: ")

    try:
        numero = float(userInput)
        quintaParte = numero / 5 # Calcula a quinta parte
        print(f"\n\U0001F389 A quinta parte de {numero} é {quintaParte} \U0001F389")
        break
    except ValueError:
        print("\u274C Valor inválido. Digite um número real! \U0001F501")
