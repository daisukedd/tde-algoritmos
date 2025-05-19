# Ler quatro notas, calcular a média aritmética e imprimir o resultado

try:
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))
    nota4 = float(input("Digite a 4ª nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"Média aritmética das quatro notas: {media:.2f}")
except ValueError:
    print("Erro: por favor, digite apenas números válidos.")
