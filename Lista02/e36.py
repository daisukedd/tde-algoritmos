def calcular_comissao(venda):
    if venda >= 100000:
        comissao = 700 + (venda * 0.16)
    elif venda >= 80000:
        comissao = 650 + (venda * 0.14)
    elif venda >= 60000:
        comissao = 600 + (venda * 0.14)
    elif venda >= 40000:
        comissao = 550 + (venda * 0.14)
    elif venda >= 20000:
        comissao = 500 + (venda * 0.14)
    else:
        comissao = 400 + (venda * 0.14)

    return comissao

# Entrada do usuário
try:
    venda = float(input("Informe o valor da venda mensal: R$ "))
    comissao = calcular_comissao(venda)
    print(f"A comissão do vendedor será: R$ {comissao:.2f}")
except ValueError:
    print("Por Favor, Insira um valor númerico válido.")