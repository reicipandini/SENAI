contador = 1
soma = 0
while contador <=3:
   salario = float(input(f"digite os salaros:  {contador} funcionarios: "));
   contador += 1
   soma += salario 
media = soma / 5
print("media de salarios dos 5 funcionarios é: ", media)