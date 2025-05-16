# Alturas iniciais de Chico e Zé
altura_chico = 1.50
altura_ze = 1.10

# Crescimentos anuais
crescimento_chico = 0.02
crescimento_ze = 0.03

anos = 0

# Enquanto Zé não ultrapassar Chico
while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    anos += 1

print(f"Serão necessários {anos} anos para que Zé seja mais alto que Chico.")