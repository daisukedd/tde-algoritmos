# Leitura de um número fornecido pelo usuário
n = float(input("Informe um número: "))

# Verifica se o número é positivo
if n > 0:
    ao_quadrado = n ** 2
    raiz = n ** 0.5

    print(f"Número ao quadrado: {ao_quadrado:.2f}")
    print(f"Raiz quadrada: {raiz:.2f}")
else:
    print("Número não é positivo. Nenhum cálculo foi realizado.")