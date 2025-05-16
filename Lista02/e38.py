def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_nascimento_valida(dia, mes, ano):
    ANO_ATUAL = 2008

    if ano > ANO_ATUAL:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    
    if mes == 2:
        if eh_bissexto(ano):
            return dia <= 29
        else:
            return dia <= 28
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    else:
        return dia <= 31

# Entrada de dados
try:
    dia = int(input("Informe o dia do nascimento: "))
    mes = int(input("Informe o mes do nascimento: "))
    ano = int(input("Informe o ano do nascimento: "))

    if data_nascimento_valida(dia, mes, ano):
        print("Data Válida.")
    else:
        print("Data Inválida.")
except ValueError:
    print("Por Favor, Insira apenas números inteiros válidos.")