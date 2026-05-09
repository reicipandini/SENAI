#Grupo 1: Monitoramento de Silo (Grãos)
#Problema: O silo começa com 500kg. A cada ciclo, uma esteira retira 50kg.
#Detalhes: O programa deve imprimir: "Retirando 50kg... Restam [X]kg".
#Objetivo Técnico: Usar um laço que subtraia um valor fixo até chegar a zero.
#Variáveis: peso_silo, retirada.

peso_silo = 500
retirada = 50
ciclo = 1

while peso_silo > 0:
    peso_silo = peso_silo - retirada

    print("Ciclo", ciclo)
    print("Retirando", retirada, "kg")
    print("Restam", peso_silo, "kg")
    print("-------------------")

    ciclo = ciclo + 1

print("Silo vazio!")