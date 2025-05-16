# Leitura de dois números inteiros fornecidos pelo usuário
n1 = float(input("Informe o primeiro número inteiro: "))
n2 = float(input("Informe o segundo número inteiro: "))

# Verifica qual é o maior e calcula a diferença
if n1 > n2:
    maior = n1
    diferenca = n1 - n2
elif n2 > n1:
    maior = n2
    diferenca = n2 - n1
else:
    maior = n1  # ou n2, já que são iguais
    diferenca = 0

# Exibe o resultado
print(f"O maior número é: {maior}")
print(f"A diferença entre eles é: {diferenca}")