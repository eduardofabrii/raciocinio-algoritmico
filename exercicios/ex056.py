# 3) Implemente um algoritmo para somar o conteúdo de duas
# matrizes bidimensionais de ordem 2 do tipo inteiro, lidas pelo
# teclado, para uma terceira matriz.

matrizUm = []
matrizDois = []
matrizTres = []

for linhas in range(2):
    linhas = []
    for colunas in range(2):
        numero = int(input('Digite um número: '))
        linhas.append(numero)
    matrizUm.append(linhas)
print(matrizUm)

for linhas in range(2):
    linhas = []
    for colunas in range(2):
        numero = int(input('Digite um número: '))
        linhas.append(numero)
    matrizDois.append(linhas)
print(matrizDois)

for linhas in range(2):
    linhaTerceiraMatriz = []
    for colunas in range(2):
        soma = matrizUm[linhas][colunas] + matrizDois[linhas][colunas]
        linhaTerceiraMatriz.append(soma)
    matrizTres.append(linhaTerceiraMatriz)
print(matrizUm)
print(matrizTres)