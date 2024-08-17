# 9. Escreva um programa que receba uma lista de números e retorne o número de elementos da lista.

lista = []

for cont in range(4):
    numero = int(input('Digite um número: '))
    lista.append(numero)
print(f'O número de elementos da lista é de: {len(lista)} elementos.')
