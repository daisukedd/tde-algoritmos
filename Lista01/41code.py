# Horas trabajadas e bônus de 10%

# Solicita o valor da hora de trabalho e o número de horas trabalhadas
valor_hora = float(input("Digite o valor da hora de trabalho (R$): "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o valor bruto - sem bônus
valor_bruto = valor_hora * horas_trabalhadas

# Calcula o bônus de 10%
bonus = valor_bruto * 0.10

# Calcula o valor total a ser pago
valor_total = valor_bruto + bonus

print(f"\n📊 Resultado")
print(f"Valor bruto (sem bônus): R$ {valor_bruto:.2f}")
print(f"Bônus de 10%: R$ {bonus:.2f}")
print(f"Valor total a ser pago: R$ {valor_total:.2f}")
