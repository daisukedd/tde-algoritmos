# Laço infinito para o menu
while True:
    print("\nCALCULADORA - MENU DE OPÇÕES")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção (1 a 5): ")

    if opcao == '5':
        print("Programa encerrado.")
        break

    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da adição: {resultado:.2f}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado:.2f}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado:.2f}")
        elif opcao == '4':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado:.2f}")
    else:
        print("Opção inválida. Tente novamente.")