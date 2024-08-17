# 1. Crie uma matriz 3x3 com elementos aleatórios e exiba-a na tela:

matriz = []

for linha in range(3):
    linha = []
    for colunas in range(3):
        numero = int(input('Digite um número: '))
        linha.append(numero)
    matriz.append(linha)

print(matriz)