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

# Determina o intervalo corretamente
inicio = min(a, b)
fim = max(a, b)

contador = 0  # Conta os primos no intervalo

for numero in range(inicio, fim + 1):
    if eh_primo(numero):
        contador += 1

print(f"Existem {contador} números primos entre {inicio} e {fim}.")