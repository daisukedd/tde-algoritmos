# Ler comprimento em jardas e converter para metros
# Uma jarda equivale a 0,914 metros ou a aproximadamente 91 centímetros

while True:
    userInput = input("Digite o comprimento em jardas (yards): ")

    try:
        jardas = float(userInput)
        metros = 0.91 * jardas
        print(f"\n\u2705 Comprimento em metros: {metros:.2f} m \u2705")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite um número válido! \U0001f501")
