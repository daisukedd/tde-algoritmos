# Conversão de acres para metros quadrados (m²)

while True:
    userInput = input("Digite uma área em acres: ")

    try:
        acres = float(userInput)
        metros_quadrados = acres * 4048.58
        print(f"\u2705 {acres} acres equivalem a {metros_quadrados:.2f} m² \u2615")
        break
    except ValueError:
        print("\u26a0 Valor inválido! Digite um número real. \u23f3")
