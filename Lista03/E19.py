# Solicita ao usuário um número entre 100 e 999
numero = int(input("Digite um número inteiro entre 100 e 999: "))

# Verifica se o número está dentro do intervalo permitido
if 100 <= numero <= 999:
    centenas = numero // 100             # Obtém o dígito das centenas
    dezenas = (numero % 100) // 10       # Obtém o dígito das dezenas
    unidades = numero % 10               # Obtém o dígito das unidades

    # Imprime cada algarismo em uma linha
    print("Centena:", centenas)
    print("Dezena:", dezenas)
    print("Unidade:", unidades)
else:
    print("Número fora do intervalo permitido.")