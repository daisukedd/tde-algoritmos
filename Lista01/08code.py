# Ler temperatura em Kelvin e converter para Celsius

while True:
    userInput = input("Digite a temperatura em graus Kelvin: ")

    try:
        kelvinTemp = float(userInput)
        celsiusTemp = kelvinTemp - 273.15 # Converte Kelvin para Celsius
        print(f"\n\U0001F321 Temperatura em Celsius: {celsiusTemp:.2f}°C \U0001F321") #.2f para limitar a 2 casas decimais
        break
    except ValueError:
        print("\u274C Valor inválido. Digite uma temperatura válida! \U0001F501")
