import random

# Gera número aleatório entre 1 e 1000
numero_secreto = random.randint(1, 1000)
tentativas = 0

print("Adivinhe o número que estou pensando (entre 1 e 1000):")

# Laço até acertar o número
while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).")
        break