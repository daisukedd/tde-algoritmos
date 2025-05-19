# Calucula a hipotenusa de um triângulo retângulo
# O cateto a e o cateto b são os lados do triângulo retângulo
# Fórmula da hipotenusa: c = √(a² + b²)

try:
    a = float(input("Digite o valor do cateto a: "))
    b = float(input("Digite o valor do cateto b: "))

    hipotenusa = (a**2 + b**2) ** 0.5  # Raiz quadrada

    print("\n📐 Resultado")
    print(f"Cateto a: {a}")
    print(f"Cateto b: {b}")
    print(f"Hipotenusa: {hipotenusa:.4f}")
except ValueError:
    print("❌ Erro: por favor, digite valores numéricos válidos.")
