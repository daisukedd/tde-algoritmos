# Solicita o valor de n
n = int(input("Digite o valor de n: "))

# -----------------------------------
# 1) Soma dos números de 1 até n
# -----------------------------------
soma1 = 0
for i in range(1, n + 1):
    soma1 += i

print("\n1) Soma dos números de 1 até n:")
print("Soma =", soma1)

# -----------------------------------
# 2) Soma alternada: 1 - 2 + 3 - 4 + ... + (2n - 1)
# -----------------------------------
soma2 = 0
for i in range(1, 2 * n):
    if i % 2 == 0:
        soma2 -= i
    else:
        soma2 += i

print("\n2) Soma da sequência 1 - 2 + 3 - 4 + ... + (2n - 1):")
print("Soma =", soma2)

# -----------------------------------
# 3) Soma dos n primeiros números ímpares: 1 + 3 + 5 + ... + (2n - 1)
# -----------------------------------
soma3 = 0
for i in range(1, 2 * n, 2):
    soma3 += i

print("\n3) Soma dos n primeiros números ímpares:")
print("Soma =", soma3)