# Dada uma matriz 2x2 de números inteiros lida pelo
# # teclado, implemente um algoritmo em Python para
# # imprimir na tela o somatório de cada linha.

matriz = []

for linhas in range(2):
    linhas = []
    for colunas in range(2):
        numero = int(input("Digite um número: "))
        linhas.append(numero)
    matriz.append(linhas)
print(matriz)


for linhas in range(2):
    soma = 0
    for colunas in range(2):
        soma += matriz[linhas][colunas]
    print(f'Na linha {linhas+1} = {soma}')

