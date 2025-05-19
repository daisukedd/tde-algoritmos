# Ler temperatura em Celsius e converter para Fahrenheit

while True:
    userInput = input("Digite a temperatura em graus Celsius: ")

    try:
        celsius = float(userInput)
        fahrenheit = celsius * (9.0 / 5.0) + 32.0 # Converte Celsius para Fahrenheit
        print(f"\n\U0001F321 Temperatura em Fahrenheit: {fahrenheit}°F \U0001F321")
        break
    except ValueError:
        print("\u274C Valor inválido. Digite uma temperatura válida! \U0001F501")
