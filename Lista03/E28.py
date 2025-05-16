# Lê o valor de N
n = int(input("Digite um número inteiro e positivo: "))

# Verifica se o número é válido
if n >= 0:
    e = 1.0      # E começa com o termo 1
    fatorial = 1 # Variável para calcular o fatorial

    for i in range(1, n + 1):
        fatorial *= i        # Calcula i!
        e += 1 / fatorial    # Soma 1/i! ao valor de E

    print(f"O valor de E para N = {n} é: {round(e, 6)}")
else:
    print("Número inválido. Digite um inteiro positivo.")