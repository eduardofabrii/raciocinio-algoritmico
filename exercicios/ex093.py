# Criar um programa que lê três temperaturas de cada mês do ano e as
# armazena em uma Matriz. Calcular a média de temperatura de cada
# mês e a média anual de temperatura, e informar quais meses ficaram
# entre as duas maiores médias mensais.

matriz = []
soma = 0
media = 0
media_anual = 0

for linhas in range(3):
    linha = []
    for colunas in range(3):
        temperatura = float(input(f'Digite a temperatura do mês {linhas+1}: '))
        linha.append(temperatura)
    matriz.append(linha)

for linhas in range(len(matriz)):
    soma = 0
    for colunas in range(len(matriz[linhas])):
        soma += matriz[linhas][colunas]
    media = soma / 3
    print(f"A média de temperatura do mês {linhas+1} é: {media}")

soma_anual = 0
for linhas in range(len(matriz)):
    for colunas in range(len(matriz[linhas])):
        soma_anual += matriz[linhas][colunas]
media_anual = soma_anual / (len(matriz) * 3)
print(f'Média anual: {media_anual}')

maiores_medias = []
maior = matriz[0][0]

for linhas in range(len(matriz)):
    for colunas in range(len(matriz[linhas])):
        soma += matriz[linhas][colunas]
    media = soma / len(matriz[linhas])
    if media > maior:
        maiores_medias = [linhas+1]
        maior = media
    elif media == maior:
        maiores_medias.append(linhas+1)

print(f'Maiores médias mensais: {maiores_medias}')
