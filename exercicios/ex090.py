# 8. Crie um programa que leia uma matriz de ordem n (números inteiros) e calcule a soma dos elementos acima da diagonal principal. Ou seja, a soma dos elementos a_ij com i < j.

def calcular_soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            soma += matriz[i][j]
    return soma

matriz =[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

result = calcular_soma_diagonal_principal(matriz)
print(result)

