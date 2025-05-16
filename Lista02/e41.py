def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif imc <= 24.9:
        return "Saudável"
    elif imc <= 29.9:
        return "Peso em Excesso"
    elif imc <= 34.9:
        return "Obesidade Grau I"
    elif imc <= 39.9:
        return "Obesidade Grau II (Severa)"
    else:
        return "Obesidade Grau III (Mórbida)"

# Entrada de dados    
try:
    peso = float(input("Informe seu peso (em kg): "))
    altura = float(input("Informe sua altura (em metros): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

except ValueError:
    print("Por Favor, Insira valores válidos para peso e altura.")