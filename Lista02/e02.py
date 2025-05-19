n = float(input("Informe um número: "))

if n >= 0:
    raiz = n**0.5
    print(f"A raiz quadrada de {n} é {raiz:.2f}")

    if n.is_integer():
        if int(n) % 2 == 0:
            print("O número informado é par.")
        else:
            print("O número informado é ímpar.")
    else:
        print(
            "O número informado não é inteiro, logo não dá para dizer se é par ou ímpar."
        )
else:
    print(
        "Número inválido! Não é possível calcular a raiz quadrada de um número negativo."
    )
