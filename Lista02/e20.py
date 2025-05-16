# Entrada dos lados
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

# Verificação se formam um triangulo
if a < b + c and b < a + c and c < a + b:
    print("Os valores formam um triangulo.")

    if a == b == c:
        print("Tipo: Triangulo Equilátero")
    elif a == b or a == c or b == c:
        print("Tipo: Triangulo Isósceles")
    else:
        print("Tipo: Triangulo Escaleno")
else:
    print("Os valores NAO formam um triangulo.")