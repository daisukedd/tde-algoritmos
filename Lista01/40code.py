# Calculo de dias trabalhados e imposto de renda

# Solicita o número de dias trabalhados
dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

# Calcula o valor bruto a ser pago
valor_bruto = dias_trabalhados * 30

# Calcula o imposto de renda (8%)
imposto = valor_bruto * 0.08

# Calcula o valor líquido (desconto do imposto)
valor_liquido = valor_bruto - imposto

print(f"\n📊 Resultado")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Imposto de Renda (8%): R$ {imposto:.2f}")
print(f"Valor líquido a ser pago: R$ {valor_liquido:.2f}")
