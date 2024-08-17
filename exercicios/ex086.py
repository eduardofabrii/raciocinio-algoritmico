# 4. Multiplique os elementos de uma matriz 2x2 por um valor escalar:

matriz = []
matrizEscalar = []

for linhas in range(2):
    linhas = []
    for colunas in range(2):
        numero = int(input('Digite um número: '))
        linhas.append(numero)
    matriz.append(linhas)

numeroMultiplicado = int(input('Digite o numero escalar: '))

for linhas in range(2):
    for colunas in range(2):
        soma = matriz[linhas][colunas] * numeroMultiplicado
        matrizEscalar.append(soma)

print(matriz)
print(matrizEscalar)
