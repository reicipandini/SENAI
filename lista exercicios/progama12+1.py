num = int(input("Número (até 3 dígitos): "))

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

print(f"CENTENA = {centena}")
print(f"DEZENA = {dezena}")
print(f"UNIDADE = {unidade}")