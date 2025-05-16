# Lê o valor de n
n = int(input("Digite um número inteiro e positivo: "))

# Verifica se o número é válido
if n > 0:
    h = 0.0  # Acumulador para o valor de H(n)
    
    for i in range(1, n + 1):
        h += 1 / i

    print(f"O valor de H({n}) é: {round(h, 4)}")
else:
    print("Número inválido. Digite um inteiro positivo.")