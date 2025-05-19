# O programa identifica a letra verificando se seu código está no *intervalo das maiúsculas na tabela ASCII (65 a 90). Depois, converte manualmente para minúscula, somando 32 ao código, e então transforma esse novo número de volta em uma letra.

try:
    letra = input("Digite uma letra MAIÚSCULA: ")

    if len(letra) != 1:
        print("❌ Digite apenas uma letra. ❌")
    else:
        codigo = ord(letra)

        if 65 <= codigo <= 90:
            minuscula = chr(codigo + 32)
            print(f"A letra '{letra}' em minúsculo é '{minuscula}'")
        else:
            print("⚠️ Isso não é uma letra maiúscula.")
except:
    print("❌ Ocorreu um erro inesperado. ❌")
