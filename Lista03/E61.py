# Função que verifica se um número é palíndromo
def eh_palindromo(n):
    # Converte o número para string e verifica se é igual ao seu reverso
    return str(n) == str(n)[::-1]

# Variável que armazena o maior palíndromo encontrado
maior_palindromo = 0
# Variáveis para armazenar os fatores do maior palíndromo
num1 = num2 = 0

# Percorre todos os pares de números de 3 dígitos (de 100 a 999)
for i in range(100, 1000):
    for j in range(i, 1000):  # Começa de i para evitar pares repetidos (ex: 123x456 e 456x123)
        produto = i * j  # Calcula o produto
        # Verifica se o produto é palíndromo e maior que o maior encontrado até agora
        if eh_palindromo(produto) and produto > maior_palindromo:
            maior_palindromo = produto  # Atualiza o maior palíndromo
            num1, num2 = i, j  # Armazena os números que geraram o palíndromo

# Exibe o resultado
print(f"O maior palíndromo feito a partir do produto de dois números de 3 dígitos é {maior_palindromo} = {num1} * {num2}")