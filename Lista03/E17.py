# Solicita um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é maior que 0
if n > 0:
    soma = 0  # Inicializa a soma
    # Soma os n primeiros números naturais (de 0 até n-1)
    for i in range(n):
        soma += i
    print(f"A soma dos {n} primeiros números naturais é: {soma}")
else:
    print("O número deve ser inteiro e positivo.")