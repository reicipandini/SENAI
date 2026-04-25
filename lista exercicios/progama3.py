
qtd_paes = int(input("Digite a quantidade de pães vendidos: "))
qtd_broas = int(input("Digite a quantidade de broas vendidas: "))


preco_pao = 0.12
preco_broa = 1.50


total = (qtd_paes * preco_pao) + (qtd_broas * preco_broa)


poupanca = total * 0.10


print(f"Total arrecadado: R$ {total:.2f}")
print(f"Valor a guardar na poupança (10%): R$ {poupanca:.2f}")