import math

def calcular_minutos(hora, minuto):
    return hora * 60 + minuto

def calcular_tarifa(tempo_em_minutos):
    horas = math.ceil(tempo_em_minutos / 60)

    if horas <= 2:
        preco = horas * 1.00
    elif horas <= 4:
        preco = 2 * 1.00 + (horas - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (horas - 4) * 2.00

    return preco

# Entrada de dados
try:
    h_chegada = int(input("Hora de Chegada: "))
    m_chegada = int(input("Minuto de Chegada: "))
    h_partida = int(input("Hora de Partida: "))
    m_partida = int(input("Minuto de Partida: "))

    minutos_chegada = calcular_minutos(h_chegada, m_chegada)
    minutos_partida = calcular_minutos(h_partida, m_partida)

    # Se a partida for no dia seguinte
    if minutos_partida < minutos_chegada:
        minutos_partida += 24 * 60  # adiciona 24 horas em minutos

    tempo_total = minutos_partida - minutos_chegada
    preco_total = calcular_tarifa(tempo_total)

    print(f"Tempo Total: {tempo_total} minutos")
    print(f"Preço Cobrado: R$ {preco_total:.2f}")

except ValueError:
    print("Por Favor, Insira valores inteiros válidos para hora e minuto.")