# Crie um programa que leia uma matriz quadrada de ordem n
#  (números inteiros) e verifique se ela é simétrica.
#  Uma matriz é simétrica se, e somente se,
#  ela é igual à sua transposta. Ou seja, se a_ij = a_ji para todo i e j. 

matriz = []

n = int(input("Digite a ordem da matriz: "))

for linhas in range(n):
    linha = []
    for colunas in range(n):
        elemento = int(input(f'Digite um número para [{linhas+1}, {colunas+1}]: '))
        linha.append(elemento)
    matriz.append(linha)

simetrica = True
for linhas in range(n):
    for colunas in range(linhas+1, n):
        if matriz[linhas][colunas] != matriz[linhas][colunas]:
            simetrica = False
            break

if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")

print(matriz)