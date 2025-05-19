x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

distancia = (x**2 + y**2) ** 0.5

print(
    "A distância do ponto (",
    int(x),
    ",",
    int(y),
    ") até a origem (0, 0) é",
    round(distancia, 2),
)
