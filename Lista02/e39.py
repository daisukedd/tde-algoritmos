def calcular_reajuste(salario):
    if salario <= 500:
        return salario * 0.25
    elif salario <= 1000:
        return salario * 0.20
    elif salario <= 1500:
        return salario * 0.15
    elif salario <= 2000:
        return salario * 0.10
    else:
        return 0    # Sem reajuste
    
def calcular_bonus(tempo_servico):
    if tempo_servico < 1:
        return 0
    elif tempo_servico <= 3:
        return 100
    elif tempo_servico <= 6:
        return 200
    elif tempo_servico <= 10:
        return 300
    else:
        return 500

# Entrada    
try:
    salario = float(input("Informe o salário atual do funcionário: R$ "))
    tempo = int(input("Informe o tempo de serviço (em anos): "))

    reajuste = calcular_reajuste(salario)
    bonus = calcular_bonus(tempo)

    if reajuste == 0 and bonus == 0:
        print("O funcionário não tem direiro a aumento.")
    else:
        salario_final = salario + reajuste + bonus
        print(f"Salário Reajustado: R$ {salario_final:.2f}")
        print(f"(Reajuste: R$ {reajuste:.2f}, Bonus: R$ {bonus:.2f})")

except ValueError:
    print("Entrada Inválida. Informe valores númericos.")