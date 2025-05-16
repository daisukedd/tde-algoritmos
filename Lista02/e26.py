# Leitura da distancia e do consumo
distancia = float(input("Informe a distancia percorrida (em KM): "))
litros = float(input("Informe a quantidade de litros de gasolina consumidos: "))

# Verificação para evitar divisão por zero
if litros == 0:
    print("Erro: Quantidade de litros não pode ser zero!")
else:
    consumo = distancia / litros
    print(f"Consumo Médio: {consumo:.2f} KM/1")

    # Classificação do consumo
    if consumo < 8:
        print("Venda o carro!")
    elif consumo <= 14:
        print("Economico!")
    else:   # consumo > 14
        print("Super Economico!")