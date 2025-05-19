def ln(x, termos=10):
    if x <= 0:
        return None
    y = (x - 1) / (x + 1)
    soma = 0
    pot = y
    for i in range(1, 2 * termos, 2):
        soma += pot / i
        pot *= y * y
    return 2 * soma


def log10(x):
    LN_10 = 2.302585
    ln_x = ln(x)

    # Se x for invalido, ln_x será None
    return ln_x / LN_10 if ln_x is not None else None


n = int(input("Digite um número inteiro maior que zero: "))
if n > 0:
    resultado = log10(n)
    if resultado is not None:
        print(f"O logaritmo base 10 de {n} é: {resultado:.4f}")
    else:
        print("Erro no cálculo do logaritmo.")
else:
    print("Número inválido. Deve ser maior que zero.")


# O termos=10 significa que vai somar os primeiros 10 termos da série. Você pode aumentar esse número para melhorar a precisão [mas vai demorar um pouco mais] ou diminuir para acelerar [mas perde precisão].
