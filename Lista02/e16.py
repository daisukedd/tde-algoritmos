print("📅 Vamos descobrir o mês correspondente ao número digitado! 🎉")

mes = int(input("Digite um número entre 1 e 12 para o mês: "))

meses = [
    "Janeiro ❄️",
    "Fevereiro 💖",
    "Março 🍀",
    "Abril 🌧️",
    "Maio 🌸",
    "Junho ☀️",
    "Julho 🎆",
    "Agosto 🏖️",
    "Setembro 🍂",
    "Outubro 🎃",
    "Novembro 🍁",
    "Dezembro 🎄",
]

if 1 <= mes <= 12:
    print(f"O mês número {mes} é {meses[mes - 1]}!")
else:
    print("⚠️ Mês inválido! Por favor, informe um número entre 1 e 12. 😉")
