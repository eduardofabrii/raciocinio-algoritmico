# Um pesquisador mediu a altura de 30 crianças e anotou em uma tabela. O seu
# objetivo é calcular a altura média das crianças, além de identificar a altura da
# maior criança bem como da menor. Sua tarefa é criar um programa em Python
# que ajude o pesquisador a realizar seu objetivo.

def calcular_media(altura, lista):
    quantidade = int(input(f'Digite a quantidade de crianças: '))
    for contador in range(quantidade):
        altura = float(input(f'Digite a altura da criança {contador+1}: '))
        lista.append(altura)
    media = altura / quantidade
    return media

def localizar_maior(lista):
    maior = lista[0]
    for contador in range(len(lista)):
        if lista[contador] > maior:
            maior = lista[contador]
    return maior

def localizar_menor(lista):
    menor = lista[0]
    for contador in range(len(lista)):
        if lista[contador] < menor:
            menor = lista[contador]
    return menor

lista_criancas = []
altura_criancas = 0

media_criancas = calcular_media(altura_criancas, lista_criancas)
maior_crianca = localizar_maior(lista_criancas)
menor_crianca = localizar_menor(lista_criancas)

print(f'\nO registro de altura das crianças é de {lista_criancas}.')
print(f'A média de altura das crianças é de {media_criancas}m.')
print(f'A maior criança tem altura de {maior_crianca}m.')
print(f'A menor criança tem altura de {menor_crianca}m.')
