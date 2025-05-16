# Inicializa acumuladores
soma_notas = 0
quantidade_notas = 0

print("Digite suas notas entre 10 e 20. Para encerrar, digite uma nota fora desse intervalo.")

while True:
    nota = float(input("Digite uma nota: "))
    
    # Verifica se a nota está no intervalo válido
    if 10 <= nota <= 20:
        soma_notas += nota
        quantidade_notas += 1
    else:
        print("Nota inválida. Encerrando entrada de dados.")
        break

# Calcula e exibe a média, se houver ao menos uma nota válida
if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print("Média aritmética das notas válidas:", round(media, 2))
else:
    print("Nenhuma nota válida foi inserida.")