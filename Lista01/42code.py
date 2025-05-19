# Salario a Receber com Gratificação e Imposto

# Solicita o salário-base do funcionário
salario_base = float(input("Digite o salário base do funcionário (R$): "))

# Calcula a gratificação de 5% sobre o salário-base
gratificacao = salario_base * 0.05

# Calcula o imposto de 7% sobre o salário-base
imposto = salario_base * 0.07

# Calcula o salário a receber
salario_final = salario_base + gratificacao - imposto

print(f"\n📊 Resultado")
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Gratificação (5%): R$ {gratificacao:.2f}")
print(f"Imposto (7%): R$ {imposto:.2f}")
print(f"Salário a receber: R$ {salario_final:.2f}")
