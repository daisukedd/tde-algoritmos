# Ler o tamanho do lado de um quadrado e imprima como resultado a sua area.
# Formula da área do quadrado: A = lado²

try:
    lado = float(input("Digite o tamanho do lado do quadrado (em metros): "))
    area = lado**2

    print("\n📐 Resultado")
    print(f"Lado do quadrado: {lado} m")
    print(f"Área do quadrado: {area:.2f} m²")

except ValueError:
    print("❌ Erro: por favor, digite um valor numérico válido.")
