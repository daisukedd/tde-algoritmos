# Entrada do usuário
preco_antigo = float(input("Informe o preço antigo do produto: R$ "))

# Cálculo do aumento conforme o preço antigo
if preco_antigo <= 50:
    aumento = 0.05
elif preco_antigo <= 100:
    aumento = 0.10
else:
    aumento = 0.15

# Calcula o novo preço
preco_novo = preco_antigo * (1 + aumento)

# Define uma mensagem com base no preço novo
if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 120:
    mensagem = "Normal"
elif preco_novo <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito Caro"

# Saída final
print(f"Preço Antigo: R$ {preco_antigo:.2f}")
print(f"Percentual de Aumento: {int(aumento * 100)}%")
print(f"Novo Preço: R$ {preco_novo:.2f}")
print(f"Classificação: {mensagem}")