# Entrada dos valores
base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio (maior que 0): "))

# Verificação das entradas
if base_maior <= 0 or base_menor <= 0 or altura <= 0:
    print("Erro: Todos os valores devem ser maiores que zero.")
else:
    # Cálculo da área do trápezio
    area = (base_maior + base_menor) * altura / 2
    print(f"A área do trapézio é: {area:.2f}")