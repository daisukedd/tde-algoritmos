# Função para calcular a média
def calcular_media(consumos):
    return sum(consumos) / len(consumos) if consumos else 0

# Entrada dos dados
num_habitantes = int(input("Digite o número de habitantes: "))
valor_kwh = float(input("Digite o valor do kWh: R$ "))

# Inicialização das variáveis
consumos = []
consumo_residencial = 0
consumo_comercial = 0
consumo_industrial = 0
maior_consumo = 0
menor_consumo = float('inf')

# Laço para coletar e processar os dados
for i in range(num_habitantes):
    consumo = float(input(f"Digite o consumo do mês do habitante {i+1} (em kWh): "))
    codigo_consumidor = int(input(f"Digite o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial) do habitante {i+1}: "))

    consumos.append(consumo)

    if consumo > maior_consumo:
        maior_consumo = consumo
    if consumo < menor_consumo:
        menor_consumo = consumo

    if codigo_consumidor == 1:
        consumo_residencial += consumo
    elif codigo_consumidor == 2:
        consumo_comercial += consumo
    elif codigo_consumidor == 3:
        consumo_industrial += consumo

# Resultados
media_consumo = calcular_media(consumos)

print(f"\nMaior consumo: {maior_consumo} kWh")
print(f"Menor consumo: {menor_consumo} kWh")
print(f"Média do consumo: {media_consumo:.2f} kWh")
print(f"\nTotal de consumo Residencial: {consumo_residencial} kWh")
print(f"Total de consumo Comercial: {consumo_comercial} kWh")
print(f"Total de consumo Industrial: {consumo_industrial} kWh")