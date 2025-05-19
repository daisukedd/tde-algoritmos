valor_total = 780000.00

# Calcular a parte de cada ganhador
parte1 = valor_total * 0.46  # Primeiro ganhador
parte2 = valor_total * 0.32  # Segundo ganhador
parte3 = valor_total - (parte1 + parte2)  # Terceiro ganhador (restante)

# Exibir os resultados
print("📊 Resultado")
print(f"Primeiro ganhador (46%): R$ {parte1:.2f}")
print(f"Segundo ganhador (32%): R$ {parte2:.2f}")
print(f"Terceiro ganhador (restante): R$ {parte3:.2f}")
