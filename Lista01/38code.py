# Salário com aumento de 25%

try:
    # Solicita o salário do funcionário
    salario_atual = float(input("Digite o salário do funcionário: R$ "))

    # Calcular o novo salário com o aumento de 25%
    aumento = salario_atual * 0.25
    novo_salario = salario_atual + aumento

    print("\n📊 Resultado")
    print(f"Salário atual: R$ {salario_atual:.2f}")
    print(f"Aumento de 25%: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")
except ValueError:
    print("❌ Erro: por favor, digite um valor numérico válido.")
