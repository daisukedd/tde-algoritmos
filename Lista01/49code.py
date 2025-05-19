def calcular_horario_termino():
    try:
        while True:
            hora = int(input("Digite a hora inicial (0-23): "))
            if 0 <= hora <= 23:
                break
            print("❌ Hora inválida! Deve estar entre 0 e 23.")

        while True:
            minuto = int(input("Digite o minuto inicial (0-59): "))
            if 0 <= minuto <= 59:
                break
            print("❌ Minuto inválido! Deve estar entre 0 e 59.")

        while True:
            segundo = int(input("Digite o segundo inicial (0-59): "))
            if 0 <= segundo <= 59:
                break
            print("❌ Segundo inválido! Deve estar entre 0 e 59.")

        while True:
            duracao = int(input("Digite a duração da experiência em segundos: "))
            if duracao >= 0:
                break
            print("❌ A duração deve ser um valor positivo.")

        total_segundos = hora * 3600 + minuto * 60 + segundo
        total_segundos += duracao
        total_segundos %= 24 * 3600

        nova_hora = total_segundos // 3600
        resto = total_segundos % 3600
        novo_minuto = resto // 60
        novo_segundo = resto % 60

        print(
            f"\n⏰ Horário de término: {nova_hora:02d}h:{novo_minuto:02d}m:{novo_segundo:02d}s"
        )

    except ValueError:
        print("❌ Por favor, digite valores inteiros válidos.")


calcular_horario_termino()
