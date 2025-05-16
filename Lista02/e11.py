# Leitura do número fornecido pelo usuário
n = int(input("Informe um número inteiro maior que zero: "))

# Verifica se o número é válido
if n > 0:
    # Converte o número para string para percorrer os dígitos
    soma = sum(int(digito) for digito in str(n))
    print(f"A soma dos algarismos de {n} é: {soma}")
else:
    print("Número inválido. O número deve ser maior que zero.")