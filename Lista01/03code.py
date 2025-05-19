# Peça ao usuario para digitar três valores inteiros e imprima a soma deles.

numeros = []  # Lista para armazenar os três números / Conceito de lista

while len(numeros) < 3: # Loop até ter três números
    userInput = input(f"Digite o {len(numeros)+1}º número inteiro: ")

    if userInput.lstrip('-').isdigit():  # Valida se é número inteiro (positivo ou negativo)
        numero = int(userInput)
        numeros.append(numero)  # Adiciona à lista
    else:
        print("\u274C Valor inválido. Digite um número inteiro! \U0001F501")  # ❌ 🔁

# Soma e exibe o resultado
soma = sum(numeros) # Se for negativo, soma normalmente!
print(f"\n\U0001F389 A soma dos três números é: {soma} \U0001F389")  # 🎉
