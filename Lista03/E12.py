# Solicita ao usuário um número inteiro positivo
N = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if N >= 0:
    print(f"\nNúmeros de {N} até 0 em ordem decrescente:")
    # Imprime os números de N até 0
    for i in range(N, -1, -1):
        print(i)
else:
    print("O número deve ser inteiro e positivo.")