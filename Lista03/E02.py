# Imprime números de 1 a 100 usando diferentes estruturas de repetição

# Usando for
print("=== Usando for ===")
for i in range(1, 101):       # De 1 a 100
    print(i)

# Usando while
print("=== Usando while ===")
i = 1
while i <= 100:               # Enquanto i <= 100
    print(i)
    i += 1                    # Incrementa i

# Usando do while (simulado)
print("=== Usando do while (simulado) ===")
i = 1
while True:                   # Loop infinito com condição de parada
    print(i)
    i += 1
    if i > 100:               # Condição para sair do loop
        break