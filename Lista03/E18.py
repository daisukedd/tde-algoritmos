# Pergunta quantos números o usuário deseja digitar
quantidade = int(input("Quantos números você deseja digitar? "))

maior = None  # Variável para armazenar o maior número
contador_maior = 0  # Contador de quantas vezes o maior número aparece

# Loop para ler os números digitados
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    # Atualiza o maior número e o contador
    if maior is None or numero > maior:
        maior = numero
        contador_maior = 1
    elif numero == maior:
        contador_maior += 1

# Exibe o maior número e quantas vezes ele foi digitado
print(f"\nO maior número lido foi: {maior}")
print(f"Ele foi lido {contador_maior} vez(es).")