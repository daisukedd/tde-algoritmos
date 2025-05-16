# Leitura das tres notas dos alunos
nota1 = float(input("Informe a nota da primeira prova: "))
nota2 = float(input("Informe a nota da segunda prova: "))
nota3 = float(input("Informe a nota da terceira prova: "))

# Calcula a média ponderada
media = (nota1 * 1 + nota2 * 1 + nota3 *2) / 4

# Exibe a média e o resultado
print(f"Média ponderada: {media:.2f}")

if media >= 6:
    print("ALUNO APROVADO!")
else:
    print("ALUNO REPROVADO!")