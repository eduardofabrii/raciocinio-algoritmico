# 6. Escreva um programa que receba
#  uma lista de números e retorne
#  uma nova lista com os números pares da lista original.

lista = []
listaPares = []

for contador in range(4):
    numeros = int(input('Digite números: '))
    lista.append(numeros)

for contador in range(len(lista)):
        if lista[contador] % 2 == 00:
            listaPares.append(lista[contador])
            
print(f'Lista com todos os números: {lista}')
print(f'Lista com os números pares: {listaPares}')

