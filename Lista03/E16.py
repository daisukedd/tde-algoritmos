# Solicita um número inteiro positivo e ímpar
N = int(input("Digite um número inteiro positivo e ímpar: "))

# Verifica se o número é positivo e ímpar
if N > 0 and N % 2 != 0:
    print(f"\nNúmeros ímpares de {N} até 1 em ordem decrescente:")
    # Imprime os números ímpares de N até 1
    for i in range(N, 0, -2):
        print(i)
else:
    print("O número deve ser inteiro, positivo e ímpar.")
