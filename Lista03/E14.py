# Solicita um número inteiro positivo e par
N = int(input("Digite um número inteiro positivo e par: "))

# Verifica se o número é positivo e par
if N > 0 and N % 2 == 0:
    print(f"\nNúmeros pares de {N} até 0 em ordem decrescente:")
    # Imprime os números pares de N até 0
    for i in range(N, -1, -2):
        print(i)
else:
    print("O número deve ser inteiro, positivo e par.")