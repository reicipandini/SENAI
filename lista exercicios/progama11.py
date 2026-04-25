dias = int(input("Dias sem acidentes: "))

anos = dias // 365
resto = dias % 365
meses = resto // 30
dias_final = resto % 30

print(f"{anos} anos, {meses} meses e {dias_final} dias")