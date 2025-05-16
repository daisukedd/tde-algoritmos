n = int(input("Digite um número inteiro maior que 1: "))  # Entrada do número

if n <= 1:
    print("O número deve ser maior que 1.")
else:
    eh_primo = True  # Assume que é primo

    # Verifica divisores até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            eh_primo = False  # Se for divisível, não é primo
            break

    # Exibe o resultado
    if eh_primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")