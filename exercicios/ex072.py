# 2. Crie um programa que receba uma lista de números e exiba o maior e o menor elemento.

lista = []

quantidade = int(input('Digite a quantidade de números: '))
for numeros in range(quantidade):
    numero = int(input('Digite um número: '))
    lista.append(numero)

maior = lista[0]
menor = lista[0]

for contador in range(len(lista)):
    if lista[contador] > 0:
        maior = lista[contador]

for contador in range(len(lista)):
    if lista[contador] < 0:
        menor = lista[contador]

print('menor', menor)
print('maior', maior)



