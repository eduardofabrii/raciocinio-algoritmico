# 3. Calcule a soma dos elementos de uma matriz 3x3:

matriz = []

for linhas in range(3):
    linhas = []
    for colunas in range(3):
        numero = int(input('Digite um número: '))
        linhas.append(numero)
    matriz.append(linhas)


soma = 0
for linhas in range(3):
    for colunas in range(3):
        soma = soma + matriz[linhas][colunas]

print(matriz)
print(soma)