# Ler velocidade em km/h e converter para m/s
# Cleanzada
while True:
    userInput = input("Digite a velocidade em km/h: ")

    try:
        kmH = float(userInput)
        mS = kmH / 3.6
        print(f"\n\U0001F3CE Velocidade em m/s: {mS:.2f} m/s \U0001F3CE")
        break
    except ValueError:
        print("\u274C Valor inválido. Digite uma velocidade válida! \U0001F501")
