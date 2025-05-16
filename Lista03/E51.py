salario = 2000.0  # Salário inicial em 1995
ano = 1996        # Ano em que o aumento começou
aumento = 0.015   # Aumento inicial de 1.5%

ano_atual = 2025  # Ano final para cálculo

# Enquanto o ano atual não for atingido
while ano <= ano_atual:
    salario += salario * aumento  # Aplica o aumento ao salário
    aumento *= 2  # O aumento dobra a cada ano
    ano += 1      # Avança para o próximo ano

# Exibe o salário final
print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")