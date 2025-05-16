import random

# Variáveis para armazenar perguntas e respostas
perguntas = []
respostas_corretas = []
respostas_aluno = []

# Geração e aplicação das 5 perguntas
for i in range(5):
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    resposta_correta = a + b

    print(f"Pergunta {i + 1}: Quanto é {a} + {b}?")
    resposta = int(input("Sua Resposta: "))

    perguntas.append ((a, b))
    respostas_corretas.append(resposta_correta)
    respostas_aluno.append(resposta)

# Verificação das respostas e resultado final
acertos = 0
print("Resultado da Prova:")
for i in range(5):
    a, b = perguntas[i]
    print(f"Pergunta {i + 1}: {a} + {b} = {respostas_corretas[i]}")
    print(f"Sua Resposta: {respostas_aluno[i]}")
    if respostas_aluno[i] == respostas_corretas[i]:
        print("Acertou!")
        acertos += 1
    else:
        print("Errou.")

print(f"Voce acertou {acertos} de 5 perguntas.")