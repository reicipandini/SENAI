#Grupo 1: Monitoramento de Silo (Grãos)
#SENAI - Aprendizagem Industrial em Programador de Sistemas da Informação
#Autores: Alice S. de Medeiros, Davi da Cruz Moreira e Reici Pandini

#Problema:
#O silo começa com uma quantidade de grãos e,
#a cada ciclo, uma esteira retira uma quantidade fixa.

#Objetivo:
#Usar um laço de repetição para diminuir o peso do silo
#até que ele fique vazio.

#Variáveis utilizadas:
#peso_silo, retirada e ciclo


print("===================================")
print("      SEJA BEM-VINDO")
print("Sistema de Monitoramento de Silo")
print("")
print("Alunos:")
print("- Alice Medeiros")
print("- Davi da Cruz")
print("- Reici Pandini")
print("===================================")



print("inicio" \
"")

# Entrada de dados
peso_silo = int(input("Digite a quantidade de grãos no silo: "))
retirada = int(input("Digite a quantidade retirada por ciclo: "))

# Contador de ciclos
ciclo = 1


# Laço de repetição enquanto houver carga no silo
while peso_silo > 0:

    print("")
    print("Ciclo", ciclo)

    # Verifica se existe quantidade suficiente para retirada
    if peso_silo < retirada:
        print("O silo não possui carga suficiente para outro ciclo!")
        print("Restam apenas", peso_silo, "kg")
        break

    # Mostra a retirada realizada
    print("Retirando", retirada, "kg...")

    # Subtração da carga retirada
    peso_silo = peso_silo - retirada

    # Exibe a quantidade restante
    print("Restam", peso_silo, "kg no silo")
    print("<*=======================*>")

    # Soma +1 ao contador de ciclos
    ciclo = ciclo + 1


print("")
print("!===== ATENÇÃO =====!")
print("Silo vazio!")
print("Não há carga para o próximo ciclo!!")


# Pergunta se o usuário deseja executar novamente
resposta = input("Deseja digitar novos valores? (s/n): ")

if resposta == "s":
    print("Reinicie o programa para novos valores.")

else:
    print("")
    print("===================================")
    print(" Obrigado por utilizar o sistema!")
    print("      Programa finalizado.")
    print("===================================")