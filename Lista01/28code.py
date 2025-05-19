# Três valores com a soma dos quadrados dos três valores lidos

print("\u270f\ufe0f Soma dos quadrados de três valores")

soma_quadrados = 0

for i in range(1, 4):  # Loop de 1 a 3
    while True:
        try:
            # Solicita o valor ao usuário
            valor = float(input(f"\u2192 Digite o {i}º valor: "))
            soma_quadrados += valor**2
            break

        # Verifica se o valor é um número real
        except ValueError:
            print("\u26a0\ufe0f Valor inválido. Digite um número real.")

print(f"\n\u2728 A soma dos quadrados é: {soma_quadrados:.2f}")
