# Solicita um número inteiro positivo e par
N = int(input("Digite um número inteiro positivo e par: "))

# Verifica se o número é positivo e par
if N > 0 and N % 2 == 0:
    print(f"\nNúmeros pares de 0 até {N} em ordem crescente:")
    # Imprime os números pares de 0 até N
    for i in range(0, N + 1, 2):
        print(i)
else:
    print("O número deve ser inteiro, positivo e par.")