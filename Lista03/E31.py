# Inicializa o somatório com 0
S = 0  
# Inicializa o numerador com 1 (primeiro número ímpar)
numerador = 1 

# Laço para o denominador de 1 até 50 (inclusive)
for denominador in range(1, 51):  
    # Adiciona a fração ao somatório
    S += numerador / denominador
    # Incrementa o numerador em 2 para o próximo número ímpar
    numerador += 2  

# Exibe o resultado formatado com duas casas decimais
print(f"O valor de S é: {S:.2f}")