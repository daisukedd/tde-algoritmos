#  Conversão de metros para jardas

while True:
    userInput = input("Digite um valor em metros: ")

    try:
        metros = float(userInput)
        jardas = metros / 0.91
        print(f"\u2705 {metros} metro(s) equivalem a {jardas:.2f} jardas \u2705")
        break
    except ValueError:
        print("\u26a0 Valor inválido! Digite um número real. \u23f3")
