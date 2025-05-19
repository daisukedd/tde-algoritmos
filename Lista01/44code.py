try:
    altura_degrau = float(input("Digite a altura do degrau (em metros): "))
    altura_objetivo = float(input("Digite a altura que deseja alcançar (em metros): "))

    if altura_degrau <= 0 or altura_objetivo <= 0:
        print("❌ Os valores devem ser maiores que zero.")
    else:
        # Divisão inteira
        degraus = int(altura_objetivo / altura_degrau)

        # Se sobrar alguma coisa, precisa de mais um degrau KK
        if altura_objetivo % altura_degrau != 0:
            degraus += 1

        # Resultado
        print("\n📏 Resultado")
        print(f"Altura do degrau: {altura_degrau:.2f} m")
        print(f"Altura desejada: {altura_objetivo:.2f} m")
        print(f"Você precisará subir {degraus} degrau(s) para atingir essa altura.")

except ValueError:
    print("❌ Erro: por favor, digite valores numéricos válidos.")
