# Ler distância em milhas e converter para quilômetros
# Uma milha equivale, aproximadamente, a 1,6093 quilômetro.

while True:
    userInput = input("Digite a distância em Milhas: ")

    try:
        milhas = float(userInput)
        km = 1.61 * milhas
        print(f"\n\U0001f699 Distância em quilômetros: {km:.2f} km \U0001f699")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite uma distância válida! \U0001f501")
