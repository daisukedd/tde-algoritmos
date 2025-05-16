numero = int(input("Informe um número inteiro: "))

# Verificação de divisibilidade
divisivel_por_3 = (numero % 3 == 0)
divisivel_por_5 = (numero % 5 == 0)

if divisivel_por_3 ^ divisivel_por_5:   # XOR lógico: verdadeiro se apenas um for verdadeiro
    print("O número é divisível por 3 ou por 5, mas não por ambos.")
else:
    print("O número NAO atende á condição (ou não é divisível por nenhum, ou é por ambos.)")