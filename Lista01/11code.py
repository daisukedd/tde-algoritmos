# Ler velocidade em m/s e converter para km/h

while True:
    userInput = input("Digite a velocidade em M/s: ")

    try:
        m_s = float(userInput)
        km_h = m_s * 3.6
        print(f"\n\U0001f3ce Velocidade em Km/h: {km_h:.2f} km/h \U0001f3ce")
        break
    except ValueError:
        print("\u274c Valor inválido. Digite uma velocidade válida! \U0001f501")
