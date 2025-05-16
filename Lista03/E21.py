# Entrada dos dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Garante que o intervalo seja sempre do menor para o maior
inicio = min(num1, num2)
fim = max(num1, num2)

soma_pares = 0
multiplicacao_impares = 1
tem_impar = False  # Para evitar multiplicação sem nenhum número ímpar

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        multiplicacao_impares *= i
        tem_impar = True

print("Soma dos números pares no intervalo:", soma_pares)
if tem_impar:
    print("Multiplicação dos números ímpares no intervalo:", multiplicacao_impares)
else:
    print("Não há números ímpares no intervalo.")