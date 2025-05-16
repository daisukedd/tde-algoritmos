# Procura valores de a, b, c tais que a < b < c e a + b + c = 1000
for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b  # Garante que a + b + c = 1000
        # Verifica se é um triplo pitagórico
        if a * a + b * b == c * c:
            print(f"Terno pitagórico encontrado: a={a}, b={b}, c={c}")
            print(f"Produto abc = {a * b * c}")
            break