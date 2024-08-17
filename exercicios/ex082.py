# 13. Escreva um programa
#  que receba uma lista 
# de números e retorne uma 
# nova lista com os elementos
#  únicos da lista original,
#  ou seja, que aparecem apenas uma vez.

lista = []
novaLista = []

for contador in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

for contador in range(len(lista)):
    if lista.count(lista[contador]) == 1:
        novaLista.append(lista[contador])

print(lista)
print(novaLista)