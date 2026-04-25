total = float(input("Valor total: R$ "))

carlos = int(total / 3)
andre = int(total / 3)
felipe = total - (carlos + andre)

print(f"Carlos: R$ {carlos:.2f}")
print(f"André: R$ {andre:.2f}")
print(f"Felipe: R$ {felipe:.2f}")