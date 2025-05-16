# Leitura da altura e do sexo da pessoa
altura = float(input("Informe sua altura (em metros): "))
sexo = input("Informe seu sexo (M para Masculino, F para Feminino): ").strip().upper()

# Calcula o peso ideal com base no sexo
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal para homem: {peso_ideal:.2f} kg")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal para mulher: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Use 'M' para Masculino ou 'F' para Feminino.")