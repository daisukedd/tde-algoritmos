# Entradas
nota = float(input("Informe a nota do aluno (0.0 a 10.0): "))
faltas = float(input("Informe o número de faltas: "))

# Determina o conceito base (até 20 faltas)
if nota >= 9.0:
    conceito = "A"
elif nota >= 7.5:
    conceito = "B"
elif nota >= 5.0:
    conceito = "C"
elif nota >= 4.0:
    conceito = "D"
else:
    conceito = "E"

# Aplica redução de conceito se faltas > 20
if faltas > 20:
    if conceito == "A":
        conceito = "B"
    elif conceito == "B":
        conceito = "C"
    elif conceito == "C":
        conceito = "D"
    elif conceito == "D":
        conceito ="E"
    # conceito E permanece E

# Saída
print(f"Nota: {nota}")
print(f"Faltas: {faltas}")
print(f"Conceito Final: {conceito}")