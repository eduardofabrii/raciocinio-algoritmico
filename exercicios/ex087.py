# 5. Crie uma matriz 4x3 com elementos digitados pelo usuário e exiba-a na tela:

matriz = []

for linhas in range(3):
    linha = []
    for colunas in range(4):
        elemento = str(input(f'Digite um texto para {linhas+1}, {colunas+1}: '))
        linha.append(elemento)
    matriz.append(linha)

print(matriz)