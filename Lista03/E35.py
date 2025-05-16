# Solicita ao usuário o intervalo
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

# Verifica se o intervalo é válido
if inicio > fim:
    print("Intervalo de valores inválido")
else:
    soma = 0
    # Soma os números ímpares dentro do intervalo
    for numero in range(inicio, fim + 1):
        if numero % 2 != 0:
            soma += numero
    print(f"Soma dos ímpares neste intervalo: {soma}")