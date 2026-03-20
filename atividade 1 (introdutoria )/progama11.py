nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while True:
    if idade > 120 or idade < 0:
        print("Idade inválida! Por favor, digite um valor maior de 0 e menor ou igual a 120.")
        idade = int(input("Digite sua idade: "))
    else:
        break 
dias_de_vida = idade * 365
print(f"Olá {nome}, você já viveu cerca de:  {dias_de_vida}")