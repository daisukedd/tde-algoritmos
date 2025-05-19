# Ler temperatura em Celsius e converter para Kelvin

while True:
    userInput = input("Digite a temperatura em graus Celsius: ")

    try:
        celsius = float(userInput)
        kelvin = celsius + 273.15 # Converte Celsius para Kelvin
        print(f"\n\U0001F321 Temperatura em Kelvin: {kelvin:.2f} K \U0001F321")
        break
    except ValueError:
        print("\u274C Valor inválido. Digite uma temperatura válida! \U0001F501")
