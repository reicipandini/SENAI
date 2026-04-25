# Entrada de dados
horas_normais = float(input("Digite a quantidade de horas normais trabalhadas: "))
horas_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))

# Cálculo do salário bruto
salario_bruto = (horas_normais * 10) + (horas_extras * 15)

# Cálculo do imposto (10%)
imposto = salario_bruto * 0.10

# Cálculo do salário líquido
salario_liquido = salario_bruto - imposto

# Saída
print("Salário bruto: R$", salario_bruto)
print("Salário líquido: R$", salario_liquido)