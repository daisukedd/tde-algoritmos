print("Escolha a opção:")
print("1 - Soma de 2 números.")
print("2 - Diferença entre 2 números (maior pelo menor).")
print("3 - Produto entre 2 números.")
print("4 - Divisão entre 2 números (o denominador não pode ser zero.)")

opcao = int(input("Opção: "))

if opcao in [1, 2, 3, 4]:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = n1 + n2
        print(f"Resultado da soma: {resultado:.2f}")
    elif opcao == 2:
        maior = max(n1, n2)
        menor = min(n1, n2)
        resultado = maior - menor
        print(f"Resultado da diferença (maior - menor): {resultado:.2f}")
    elif opcao == 3:
        resultado = n1 * n2
        print(f"Resultado do produto: {resultado:.2f}")
    elif opcao == 4:
        if n2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            resultado = n1 / n2
            print(f"Resultado da divisão: {resultado:.2f}")
else:
    print("Opção inválida. Tente novamente.")