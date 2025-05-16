# Leitura do salário e do valor da prestação
salario = float(input("Informe o salário do trabalhador: "))
prestacao = float(input("Informe o valor da prestação do empréstimo: "))

# Calcula 20% do salário
limite = salario * 0.20

# Verifica se a prestação ultrapassa 20% do salário
if prestacao > limite:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")