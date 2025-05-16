# Laço infinito do menu
while True:
    print("\nCONVERSOR DE VELOCIDADE")
    print("1 - Converter km/h para m/s")
    print("2 - Converter m/s para km/h")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        kmh = float(input("Digite a velocidade em km/h: "))
        ms = kmh / 3.6
        print(f"{kmh} km/h é igual a {ms:.2f} m/s")
    
    elif opcao == '2':
        ms = float(input("Digite a velocidade em m/s: "))
        kmh = ms * 3.6
        print(f"{ms} m/s é igual a {kmh:.2f} km/h")
    
    elif opcao == '3':
        print("Programa finalizado.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")