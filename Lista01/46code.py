try:
    # Solicitar o valor total da venda
    numero = int(input("Digite um número inteiro de três dígitos (entre 100 e 999): "))

    # Verificar se o número está no intervalo de 100 a 999
    if 100 <= numero <= 999:
        # Separar os dígitos manualmente
        centena = numero // 100
        dezena = (numero % 100) // 10
        unidade = numero % 10

        # Inverter os dígitos
        numero_invertido = (unidade * 100) + (dezena * 10) + centena

        print("\n📊 Resultado")
        print(f"Número Lido: {numero}")
        print(f"Número Gerado - Invertido: {numero_invertido}")
    else:
        print("❌ Erro: O número deve ter exatamente três dígitos (entre 100 e 999).")

except ValueError:
    print("❌ Erro: Por favor, digite um número inteiro válido.")
