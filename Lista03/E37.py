# Percorre os números de 1000 a 9999 (quatro dígitos)
for numero in range(1000, 10000):
    parte_alta = numero // 100      # Obtém os dois primeiros dígitos
    parte_baixa = numero % 100      # Obtém os dois últimos dígitos
    soma = parte_alta + parte_baixa
    # Verifica se o quadrado da soma das partes é igual ao número original
    if soma * soma == numero:
        print(numero)