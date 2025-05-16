import math

# Laço infinito
while True:
    # Solicita um número ao usuário
    valor = float(input("Digite um número positivo (0 ou negativo para sair): "))

    # Encerra se o valor for 0 ou negativo
    if valor <= 0:
        print("Encerrando o programa.")
        break

    # Calcula quadrado, cubo e raiz quadrada do valor
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz = math.sqrt(valor)

    # Exibe os resultados
    print(f"Valor: {valor}")
    print(f"Quadrado: {quadrado:.2f}")
    print(f"Cubo: {cubo:.2f}")
    print(f"Raiz quadrada: {raiz:.2f}\n")