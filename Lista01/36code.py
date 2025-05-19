# Calculo do volume de um cilindro

try:
    # Solicitar ao usuário os valores de altura e raio
    raio = float(input("Digite o valor do raio do cilindro: "))
    altura = float(input("Digite o valor da altura do cilindro: "))

    # Definir o valor de π
    pi = 3.141592

    # Calcular o volume do cilindro
    volume = pi * (raio**2) * altura

    print("\n📊 Resultado")
    print(f"Raio: {raio}")
    print(f"Altura: {altura}")
    print(f"Volume do cilindro: {volume:.4f} m³")
except ValueError:
    print("❌ Erro: por favor, digite valores numéricos válidos.")
