# Ler temperatura em Fahrenheit e converter para Celsius

while True:
    userInput = input("Digite a temperatura em graus Fahrenheit: ")

    try:
        fahrenheit = float(userInput)
        celsius = 5.0 * (fahrenheit - 32.0) / 9.0 # Converte Fahrenheit para Celsius
        print(f"\n\U0001F321 Temperatura em Celsius: {celsius:.2f}°C \U0001F321")
        break
    except ValueError: # Se não for possível converter para float
        print("\u274C Valor inválido. Digite uma temperatura válida! \U0001F501")
