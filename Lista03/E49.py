# Entradas do usuário
salario_carlos = float(input("Digite o salário de Carlos: "))
taxa_carlos = float(input("Digite a taxa de rendimento de Carlos (%): ")) / 100
taxa_joao = float(input("Digite a taxa de rendimento de João (%): ")) / 100

# Salário inicial de João é 1/3 do de Carlos
salario_joao = salario_carlos / 3

# Valores iniciais aplicados
valor_carlos = salario_carlos
valor_joao = salario_joao

meses = 0

# Enquanto João não alcançar Carlos
while valor_joao <= valor_carlos:
    valor_carlos += valor_carlos * taxa_carlos
    valor_joao += valor_joao * taxa_joao
    meses += 1

print(f"Serão necessários {meses} meses para que João ultrapasse ou iguale Carlos.")