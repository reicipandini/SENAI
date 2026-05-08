latas = int(input("Quantidade de latas (350ml): "))
garrafas600 = int(input("Quantidade de garrafas (600ml): "))
garrafas2L = int(input("Quantidade de garrafas (2L): "))

total_litros = (latas * 0.35) + (garrafas600 * 0.6) + (garrafas2L * 2)

print("Total de litros:", total_litros)