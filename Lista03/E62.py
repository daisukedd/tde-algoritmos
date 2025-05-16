# Função que retorna a representação por extenso dos números de 1 a 99
def numero_por_extenso(n):
    # Lista de palavras para os números até 19
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", 
                "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", 
                "dezoito", "dezenove"]
    # Lista para as dezenas
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", 
               "oitenta", "noventa"]

    # Se o número for menor que 20, retorna diretamente da lista unidades
    if n < 20:
        return unidades[n]
    else:
        dezena = n // 10  # Parte da dezena
        unidade = n % 10  # Parte da unidade
        if unidade == 0:
            return dezenas[dezena]  # Ex: 30, 40, etc.
        else:
            return dezenas[dezena] + '-' + unidades[unidade]  # Ex: trinta-e-um

# Função que retorna a representação por extenso dos números de 100 a 999
def centenas_por_extenso(n):
    # Lista de centenas
    centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", 
                "seiscentos", "setecentos", "oitocentos", "novecentos"]

    if n == 100:
        return "cem"  # Caso especial para 100
    else:
        centena = n // 100  # Parte da centena
        resto = n % 100     # Resto da divisão
        if resto == 0:
            return centenas[centena]  # Ex: duzentos
        else:
            return centenas[centena] + " e " + numero_por_extenso(resto)  # Ex: duzentos e um

# Função principal que soma o número de letras de 1 até 1000 escritos por extenso
def contar_letras():
    total_letras = 0

    # Conta letras dos números de 1 a 99
    for i in range(1, 100):
        total_letras += len(numero_por_extenso(i).replace(" ", "").replace("-", ""))

    # Conta letras dos números de 100 a 999
    for i in range(100, 1000):
        total_letras += len(centenas_por_extenso(i).replace(" ", "").replace("-", ""))

    # Adiciona letras do número 1000 ("mil")
    total_letras += len("mil")

    return total_letras

# Chamada da função e exibição do resultado
total_letras = contar_letras()
print(f"O total de letras utilizadas para escrever os números de 1 a 1000 é: {total_letras}")