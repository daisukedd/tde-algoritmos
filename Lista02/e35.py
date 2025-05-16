def eh_bissexto(ano):
    # Um ano é bissexto se for divisível por 4 e (não for divisível por 100 ou for divisível por 400)
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_valida(dia, mes, ano):
    # Verifica se o mes é válido
    if mes < 1 or mes > 12:
        return False
    
    # Define os dias de cada mes
    if mes == 2:
        if eh_bissexto(ano):
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    else:
        dias_no_mes = 31

    # Verifica se o dia é válido
    return 1 <= dia <= dias_no_mes

# Entrada de dados
try:
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mes: "))
    ano = int(input("Informe o ano: "))

    # Validação
    if data_valida(dia, mes, ano):
        print("Data Válida.")
    else:
        print("Data Inválida.")
except ValueError:
    print("Por favor, informe apenas números inteiros válidos.")