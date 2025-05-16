# Início de um laço infinito
while True:
    # Solicita o valor da resistência R1 ao usuário
    R1 = float(input("Digite o valor de R1 (0 para sair): "))
    # Solicita o valor da resistência R2 ao usuário
    R2 = float(input("Digite o valor de R2 (0 para sair): "))

    # Se R1 ou R2 forem zero, encerra o programa
    if R1 == 0 or R2 == 0:
        print("Encerrando o programa.")
        break

    # Calcula a resistência equivalente em paralelo
    R = (R1 * R2) / (R1 + R2)
    # Exibe o resultado com duas casas decimais
    print(f"A resistência equivalente em paralelo é: {R:.2f} ohms\n")