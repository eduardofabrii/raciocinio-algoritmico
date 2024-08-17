# 7. Crie um programa que leia duas matrizes de ordem n (números inteiros) e verifique se elas são iguais. Duas matrizes são iguais se, e somente se, elas possuem a mesma ordem e seus elementos correspondentes são iguais.

matriz1 = []
matriz2 = []

ordem1 = int(input('Digite a ordem da 1° matriz: '))

for linhas in range(ordem1):
    linha = []
    for colunas in range(ordem1):
        numero = int(input(f'Digite o número {linhas+1}, {colunas+1}: '))
        linha.append(numero)
    matriz1.append(linha)
    

ordem2 = int(input('Digite a ordem da 2° matriz: '))

for linhas in range(ordem2):
    linha = []
    for colunas in range(ordem2):
        numero = int(input(f'Digite o número {linhas+1}, {colunas+1}: '))
        linha.append(numero)
    matriz2.append(linha)

print(matriz1)
print(matriz2)

if ordem1 != ordem2:
    print('\nOrdens diferentes.')
else:
    print('\nOrdens iguais.')

iguais = True
for linhas in range(ordem1):
    for colunas in range(ordem1):
        if matriz1[linhas][colunas] != matriz2[linhas][colunas]:
            iguais = False
            break

if iguais:
    print('\nElementos iguais.')
else:
    print('\nElementos diferentes.')


        
    