# 10. Escreva um
#  programa que receba uma
#  lista de nomes e retorne o nome mais longo.
lista = []

for cont in range(4):
    nome = str(input('Digite um nome: '))
    lista.append(nome)

maior = lista[0]
for cont in range(len(lista)):
    if len(lista[cont]) > len(maior):
        maior = lista[cont]

print(f'O nome mais longo é {maior}')
