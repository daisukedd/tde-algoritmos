def converter_segundos():
    try:
        segundos = int(input("⏳ Digite o tempo em segundos: "))

        if segundos < 0:
            print("❌ O valor deve ser um número inteiro positivo.")
            return

        dias = segundos // 86400  # 1 dia tem 86400 segundos
        resto_dia = segundos % 86400

        horas = resto_dia // 3600
        minutos = (resto_dia % 3600) // 60
        segundos_restantes = resto_dia % 60

        print("\n🕒 Tempo convertido:")
        print(f"{dias:02d}d:{horas:02d}h:{minutos:02d}m:{segundos_restantes:02d}s")

    except ValueError:
        print("❌ Erro: digite apenas números inteiros válidos.")


converter_segundos()
