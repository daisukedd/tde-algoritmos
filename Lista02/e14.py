# Entrada das tres notas
trabalho = float(input("Informe a nota do Trabalho de Laboratório (0 a 10): "))
avaliacao = float(input("Informe a nota da Avaliação Semestral (0 a 10): "))
exame = float(input("Informe a nota do Exame Final (0 a 10): "))

# Verificação de validade das notas
if not (0 <= trabalho <= 10) or not (0 <= avaliacao <= 10) or not (0 <= exame <= 10):
    print("Erro: Todas as notas devem estar entre 0 e 10.")
else:
    # Cálculo da média ponderada
    media = (trabalho * 2 + avaliacao * 3 + exame * 5) / 10

    # Verificação da situação do aluno
    print(f"Média Final: {media:.1f}")

    if media < 3:
        print("Situação: Reprovado")
    elif media < 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Aprovado")