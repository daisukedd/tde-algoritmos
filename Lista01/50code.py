def calcularAnoNascimento():
    while True:
        try:
            idade = int(input("Digite a idade da pessoa (anos): "))
            if idade < 0:
                print("❌ Idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("❌ Por favor, digite um número inteiro válido para a idade.")

    while True:
        try:
            ano_atual = int(input("Digite o ano atual: "))
            if ano_atual < 0:
                print("❌ Ano inválido. Tente novamente.")
                continue
            break
        except ValueError:
            print("❌ Por favor, digite um número inteiro válido para o ano.")

    ano_nascimento = ano_atual - idade
    print(f"A pessoa nasceu em {ano_nascimento}.")


calcularAnoNascimento()
