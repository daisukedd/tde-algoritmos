# Imprimir a área de um círculo dado o raio
# Formula da área do círculo: A = π * r²

try:
    raio = float(input("Digite o valor do raio do círculo (em metros): "))
    pi = 3.141592
    area = pi * (raio**2)

    print("\n🟠 Resultado")
    print(f"Raio do círculo: {raio} m")
    print(f"Área do círculo: {area:.4f} m²")

except ValueError:
    print("❌ Erro: por favor, digite um valor numérico válido.")
