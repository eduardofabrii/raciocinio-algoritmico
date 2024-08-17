# 1. Crie um programa que receba uma lista de números e exiba a soma de seus elementos.

lista = []
soma = 0

quantidade = int(input('Digite a quantidade de números: '))
for numeros in range(quantidade):
    numero = float(input(f'Digite o número {numeros+1}: '))
    lista.append(numero)

for numeros in range(len(lista)):
    soma += lista[numeros]

print(soma)