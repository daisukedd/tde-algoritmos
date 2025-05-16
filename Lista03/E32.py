import random

# Solicita ao usuário quantas vezes deseja lançar os dados
n = int(input("Quantas vezes deseja lançar os dados? "))

# Executa os lançamentos de dados n vezes
for i in range(1, n + 1):
    d1 = random.randint(1, 6)  # Sorteia um número entre 1 e 6 para o dado 1
    d2 = random.randint(1, 6)  # Sorteia um número entre 1 e 6 para o dado 2

    # Verifica a relação entre os dois dados sorteados
    if d1 > d2:
        relacao = ">"
    elif d1 < d2:
        relacao = "<"
    else:
        relacao = "="

    # Exibe os resultados e a relação entre os dados
    print(f"Lançamento {i}: Dado 1 = {d1}, Dado 2 = {d2} --> {d1} {relacao} {d2}")