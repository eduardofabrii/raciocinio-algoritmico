# 2) Imprimir o conteúdo de uma matriz bidimensional de
# ordem 5 a partir da última linha e última coluna em direção a
# primeira linha e primeira coluna. O conteúdo da matriz deve
# ser lido previamente do teclado.

matriz = []

for linha in range(3):
    linha = []
    for coluna in range(3):
        numero = int(input(f'Insira um número para a matriz: '))
        linha.append(numero)
    matriz.append(linha)

for linha in range(2, -1, -1):
    for coluna in range(2, -1, -1):
        print(f'{matriz[linha][coluna]:<3}', end='')
    print()

