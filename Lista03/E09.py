# Imprime os N primeiros números naturais ímpares

N = int(input("Digite um número inteiro N: "))
contador = 0
numero = 1

print(f"\nOs {N} primeiros números naturais ímpares são:")

while contador < N:                  # Até imprimir N ímpares
    print(numero)
    numero += 2                      # Próximo ímpar
    contador += 1