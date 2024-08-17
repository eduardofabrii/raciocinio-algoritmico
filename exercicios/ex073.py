# 3. Crie um programa que receba duas listas de números de mesmo tamanho e crie uma terceira lista com a soma dos elementos correspondentes de cada lista.


lista1 = []
lista2 = []
lista3 = []
soma = 0

for lista in range(5):
    numero = float(input(f'Digite o número do elemento {lista+1} para a lista 01: '))
    lista1.append(numero)

for lista in range(5):
    numero = float(input(f'Digite o número do elemento {lista+1} para a lista 02: '))
    lista2.append(numero)

for lista in range(5):
    soma = lista1[lista] + lista2[lista]
    lista3.append(soma)

print(lista3)