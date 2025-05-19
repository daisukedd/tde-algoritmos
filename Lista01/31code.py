# Ler um número inteiro e imprimir o seu antecessor e o seu sucessor

try:
    # Ler um número inteiro
    numero = int(input("Digite um número inteiro: "))
    antecessor = numero - 1  # Calcular o antecessor
    sucessor = numero + 1  # Calcular o sucessor

    print("\n📊 Resultado")
    print(f"Número digitado: {numero}")
    print(f"Antecessor: {antecessor}")
    print(f"Sucessor: {sucessor}")
except ValueError:
    print("❌ Erro: por favor, digite um número inteiro válido.")
