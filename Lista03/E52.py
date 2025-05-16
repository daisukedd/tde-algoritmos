valor = int(input("Digite o valor do saque: R$ "))  # Solicita o valor do saque

notas = [100, 50, 20, 10, 5, 2, 1]  # Tipos de notas disponíveis

print("Notas fornecidas:")

# Laço para calcular a quantidade de cada nota
for nota in notas:
    quantidade = valor // nota  # Quantas notas daquela são necessárias
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {nota}")
        valor %= nota  # Atualiza o valor restante para saque