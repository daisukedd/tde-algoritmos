print("=== Calculadora Básica ===")
print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada (1 a 4): "))

if opcao in [1, 2, 3, 4]:
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))

    match opcao:
        case 1:
            resultado = n1 + n2
            operacao = "Adição"
        case 2:
            resultado = n1 - n2
            operacao = "Subtração"
        case 3:
            resultado = n1 * n2
            operacao = "Multiplicação"
        case 4:
            if n2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                exit()
            resultado = n1 / n2
            operacao = "Divisão"

    print(f"Resultado da {operacao}: {resultado:.2f}")
else:
    print("Opção inválida. Encerrando o programa.")