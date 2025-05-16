# Solicita ao usuário um número inteiro positivo
N = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if N >= 0:
    print(f"\nNúmeros de 0 até {N} em ordem crescente:")
    # Imprime os números de 0 até N
    for i in range(N + 1):
        print(i)
else:
    print("O número deve ser inteiro e positivo.")