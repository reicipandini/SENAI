frangos = int(input("digite a quantidade de frangos: "))

custo_chip = 4.0
custo_alimento = 3.50

gasto_por_frango = custo_chip + (2 * custo_alimento)
gasto_total = frangos * gasto_por_frango

print("a quantia de frangos na fazenda é:", frangos)
print("para colocar a quantia desejada de frangos sera preciso gastar:", gasto_total)