# 11. Escreva um programa que receba duas listas e 
# retorne uma nova lista com os elementos comuns às duas listas.

lista1 = []
lista2 = []
lista3 = []

for cont in range(4):
    numero = int(input(f'Digite o número {cont+1} para a lista 01: '))
    lista1.append(numero)

for cont in range(4):
    numero = int(input(f'Digite o número {cont+1} para a lista 02: '))
    lista2.append(numero)

for cont in range(len(lista1)):
    if lista1[cont] == lista2[cont]:
        lista3.append((lista1[cont], lista2[cont]))

print(f'A terceira lista foi criada com o número em comum da lista 01 e lista 02, que são: {lista3}')

