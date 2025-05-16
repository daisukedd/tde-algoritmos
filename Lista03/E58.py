# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Entrada dos limites
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

inicio = min(a, b)
fim = max(a, b)

soma = 0  # Soma dos primos

# Percorre o intervalo e soma os primos
for numero in range(inicio, fim + 1):
    if eh_primo(numero):
        soma += numero

print(f"A soma dos números primos entre {inicio} e {fim} é: {soma}")