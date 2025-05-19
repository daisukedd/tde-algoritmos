# Conversão de Reais para Dólares
# Cotação do dólar: 5.10 em 13/05/2025

try:
    valorReais = float(input("Digite o valor em reais (R$): "))
    cotacaoDolar = float(input("Digite a cotação do dólar (ex: 5.10): "))

    valorConvertido = valorReais / cotacaoDolar

    print("\n💰 Conversão de Moeda 💰")
    print(f"R$ {valorReais:.2f} equivalem a aproximadamente 💵 ${valorConvertido:.2f}")
except ValueError:
    print("❌ Erro: por favor, digite valores numéricos válidos.")
