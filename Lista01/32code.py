# Ler um numero inteiro e imprimir a soma do sucessor de seu triplo com o antecessor de seu dobro??? oxe kkk

try:
    n = int(input("Digite um número inteiro: "))

    triplo_sucessor = 3 * n + 1
    dobro_antecessor = 2 * n - 1
    resultado = triplo_sucessor + dobro_antecessor

    print("\n📊 Resultado")
    print(f"Triplo de {n} + 1 (sucessor): {triplo_sucessor}")
    print(f"Dobro de {n} - 1 (antecessor): {dobro_antecessor}")
    print(f"Soma final: {resultado}")

except ValueError:
    print("❌ Erro: por favor, digite um número inteiro válido.")
