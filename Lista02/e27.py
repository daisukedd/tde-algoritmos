# Entrada da idade
idade = int(input("Informe a idade do nadador: "))

# Verifica a categoria
if idade >= 5 and idade <= 7:
    print("Categoria: infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Senior")
else:
    print("Idade abaixo da mínima para classificação.")