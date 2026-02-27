nome = input("insira o nome do aluno:")
nota1 = float(input("insira a nota do primerio semestre:"))
nota2 = float(input("insira a nota do segundo semestre:"))


media = (nota1+nota2)/2
print("o aluno ",nome," media de final do ano : ",media)

if media >= 7:
        print("o aluno esta  aprovado")
elif media >= 5:
    print("o aluno esta em recuperaçao")

else:
   print(" o aluno esta reprovado")
