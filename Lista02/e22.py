# Entrada dos dados
idade = int(input("Informe a idade do trabalhador: "))
tempo_servico = int(input("Informe o tempo de serviço (em anos): "))

# Verificação das condições de aposentadoria
if idade >= 65:
    print("Pode se aposentar (tem 65 anos ou mais).")
elif tempo_servico >= 30:
    print("Pode se aposentar (tem 30 anos ou mais de serviço).")
elif idade >= 60 and tempo_servico >= 25:
    print("Pode se aposentar (tem pelo menos 60 anos e 25 anos de serviço).")
else:
    print("Não pode se aposentar ainda.")