c = float(input("Digite o comprimento do terreno (em metros): "))
l = float(input("Digite a largura do terreno (em metros): "))

p = float(input("Digite o preço do metro de tela (R$): "))

perimetro = 2 * (c + l)

custo = perimetro * p

print(f"\nO custo para cercar o terreno será: R$ {custo:.2f}")
