# Soma dos 50 primeiros números pares

soma = 0
numero = 0
contador = 0

while contador < 50:      # Enquanto não somar 50 números
    soma += numero        # Soma o número atual
    numero += 2           # Vai para o próximo par
    contador += 1

print(f"A soma dos 50 primeiros números pares é: {soma}")