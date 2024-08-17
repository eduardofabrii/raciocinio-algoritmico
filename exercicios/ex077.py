# 7. Escreva um programa
#  que receba uma lista
#  de palavras e retorne
#  uma nova lista com as palavras
#  que começam com a letra 'a'.

lista = []
lista_inicialA = []

for contador in range(4):
    texto = str(input('Digite uma palavra: '))
    lista.append(texto)

for palavra in range(len(lista)):
    if lista[palavra][0] == 'a':
        lista_inicialA.append(lista[palavra])

print(f'Lista de palavras: {lista}')
print(f'Lista de palavras que começam com A: {lista_inicialA}')