# 14. Crie um programa
#  em Python que leia do
#  teclado uma lista de
#  números inteiros e exiba a soma desses números.

lista = []

for contador in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

soma = 0
for contador in range(len(lista)):
    soma = soma + lista[contador]

print(soma)