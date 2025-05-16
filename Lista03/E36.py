# Inicializa variáveis
soma_dos_quadrados = 0  # Soma dos quadrados de 1 a 100
soma = 0                # Soma simples de 1 a 100

# Laço para os 100 primeiros números naturais
for i in range(1, 101):
    soma_dos_quadrados += i ** 2
    soma += i

quadrado_da_soma = soma ** 2          # Calcula o quadrado da soma
diferenca = quadrado_da_soma - soma_dos_quadrados  # Diferença entre os dois valores

print(f"Diferença: {diferenca}")