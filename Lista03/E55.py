# Função que verifica se um número é primo
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro não negativo: "))  # Entrada do número

if n < 0:
    print("Número inválido. Digite um valor não negativo.")
else:
    contador = 0  # Conta quantos primos foram encontrados
    numero = 2    # Começa pelo primeiro primo
    soma = 0      # Soma dos primos

    while contador < n:
        if eh_primo(numero):
            soma += numero
            contador += 1
        numero += 1

    print(f"A soma dos {n} primeiros números primos é: {soma}")