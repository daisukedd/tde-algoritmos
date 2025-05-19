# Valor de área em hectares convertido em metros quadrados.

while True:
    try:
        hectares = float(input("🌾 Digite a área em hectares:  "))
        metros_quadrados = hectares * 10000
        print(f"\u2705 A área em metros quadrados é: {metros_quadrados:.2f} m² 🌾")
        break
    except ValueError:
        print(
            "\u26a0\ufe0f Valor inválido! Digite um número real (use ponto se necessário)."
        )
