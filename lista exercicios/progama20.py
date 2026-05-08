blusas = int(input("Quantidade de blusas: "))

metros_por_blusa = 120
metros_novelo = 125

metros_total = blusas * metros_por_blusa
novelos = metros_total / metros_novelo

if metros_total % metros_novelo != 0:
    novelos = int(novelos) + 1

print("Metros de lã necessários:", metros_total)
print("Quantidade de novelos necessários:", novelos)