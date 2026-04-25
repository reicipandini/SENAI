
preco_litro = float(input("Digite o preço do litro da gasolina: R$ "))
valor_pago = float(input("Digite o valor que deseja abastecer: R$ "))

litros = valor_pago / preco_litro

print(f"Você conseguiu abastecer {litros:.2f} litros de gasolina.")