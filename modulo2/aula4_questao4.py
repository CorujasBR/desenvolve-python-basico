

cem = cinquenta = vinte = dez = cinco = dois = 0


reais = int(input("Entre com o valor em dinheiro: "))


if reais >= 100:
    cem = reais // 100
    reais = reais % 100

if reais >= 50:
    cinquenta = reais // 50
    reais = reais % 50

if reais >= 20:
    vinte = reais // 20
    reais = reais % 20

if reais >= 10:
    dez = reais // 10
    reais = reais % 10

if reais >= 5:
    cinco = reais // 5
    reais = reais % 5

if reais >= 2:
    dois = reais // 2
    reais = reais % 2


print("Valor foi dividido em:")
print(f"Nota(s) de 100: {cem}")
print(f"Nota(s) de 50: {cinquenta}")
print(f"Nota(s) de 20: {vinte}")
print(f"Nota(s) de 10: {dez}")
print(f"Nota(s) de 5: {cinco}")
print(f"Nota(s) de 2: {dois}")
