# Conversão de metros quadrados (m²) para hectares
# Um hectare equivale a 10.000 metros quadrados.

while True:
    userInput = input("Digite o valor da área em metros quadrados (m²): ")

    try:
        metros_quadrados = float(userInput)  # Converte a entrada para número real
        hectares = metros_quadrados * 0.0001  # Fórmula: H = M * 0.0001
        print(
            f"\u2705 {metros_quadrados} m² equivalem a {hectares:.4f} hectares \u2705"
        )
        break
    except ValueError:
        print("\u26a0 Valor inválido! Digite um número real. \u23f3")
