#  Conversão de metros quadrados (m²) para acres
# Um acre equivale a 4046.86 metros quadrados.

while True:
    userInput = input("Digite uma área em metros quadrados (m²): ")

    try:
        metros_quadrados = float(userInput)
        acres = metros_quadrados * 0.000247
        print(f"\u2705 {metros_quadrados} m² equivalem a {acres:.6f} acres \u2705")
        break
    except ValueError:
        print("\u26a0 Valor inválido! Digite um número real. \u23f3")
