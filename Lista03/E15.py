# Solicita um número inteiro positivo e ímpar
N = int(input("Digite um número inteiro positivo e ímpar: "))

# Verifica se o número é positivo e ímpar
if N > 0 and N % 2 != 0:
    print(f"\nNúmeros ímpares de 1 até {N} em ordem crescente:")
    # Imprime os números ímpares de 1 até N
    for i in range(1, N + 1, 2):
        print(i)
else:
    print("O número deve ser inteiro, positivo e ímpar.")
