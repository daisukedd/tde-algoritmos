investidor1 = float(input("Quanto investiu o primeiro amigo? R$ "))
investidor2 = float(input("Quanto investiu o segundo amigo? R$ "))
investidor3 = float(input("Quanto investiu o terceiro amigo? R$ "))

premio = float(input("Qual o valor total do prêmio? R$ "))

total_investido = investidor1 + investidor2 + investidor3

ganho1 = premio * (investidor1 / total_investido)
ganho2 = premio * (investidor2 / total_investido)
ganho3 = premio * (investidor3 / total_investido)

print(f"\nO primeiro amigo receberá: R$ {ganho1:.2f}")
print(f"O segundo amigo receberá: R$ {ganho2:.2f}")
print(f"O terceiro amigo receberá: R$ {ganho3:.2f}")
