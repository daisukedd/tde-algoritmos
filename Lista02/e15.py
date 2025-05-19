print("===! Descubra o dia da semana !===")

numero = int(input("Informe um número inteiro entre 1 e 7: "))

# Cada dia da semana corresponde a um número
dias = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
]

if 1 <= numero <= 7:
    print(f"O dia da semana correspondente ao número {numero} é: {dias[numero - 1]}")
else:
    print("Oops! Número inválido. Por favor, informe um número entre 1 e 7.")
