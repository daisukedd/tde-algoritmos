# Ler distância em quilômetros e converter para milhas

while True:
    userInput = input("Digite a distância em quilômetros: ")

    try:
        km = float(userInput)
        milhas = km / 1.61
        print(f"\n\U0001f699 Distância em milhas: {milhas:.2f} mi \U0001f699")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite uma distância válida! \U0001f501")
