# Imprime os primeiros 5 múltiplos de 3
multiplo = 1           # Variável declarada, mas não utilizada
contador = 0           # Contador de múltiplos encontrados

for numero in range(1, 100):  # Loop de 1 até 99
    if numero % 3 == 0:       # Verifica se o número é múltiplo de 3
        print(numero)         # Exibe o número
        contador += 1         # Incrementa o contador
    if contador == 5:         # Se já encontrou 5 múltiplos, encerra o loop
        break