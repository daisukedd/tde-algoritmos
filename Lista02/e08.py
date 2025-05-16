# Leitura das duas notas
nota1 = float(input("Informe a primeira nota (entre 0.0 e 10.0): "))
nota2 = float(input("Informe a segunda nota (entre 0.0 e 10.0): "))

# Verifica se ambas as notas são válidas
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota1 + nota2) / 2
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nota inválida! As notas devem estar entre 0.0 e 10.0. Programa encerrado.")