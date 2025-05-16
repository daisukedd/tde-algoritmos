# Lê 10 números inteiros positivos com validação e calcula a média

numeros = []                         # Lista para armazenar

while len(numeros) < 10:             # Até ter 10 números válidos
    try:
        numero = int(input(f"Digite o {len(numeros)+1}º número inteiro positivo: "))
        if numero > 0:               # Verifica se é positivo
            numeros.append(numero)
        else:
            print("Apenas números inteiros **positivos** são aceitos. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

media = sum(numeros) / len(numeros)  # Média dos números
print(f"\nNúmeros válidos digitados: {numeros}")
print(f"Média dos números positivos: {media}")