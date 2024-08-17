# 4. Crie um programa que receba uma lista de strings
#  e exiba apenas as strings com mais de 5 caracteres.

lista = []

print('Digite "parar" para encerrar.')
texto = 0

while texto != "parar":
    texto = input('Digite o texto: ')
    if len(texto) > 5:
        lista.append(texto)
    else:
        print('Palavra menor que cinco letras.\n')

print(f'Palavras menores que cinco letras: {lista}')

# lista = []
# lista2 = []

# for contador in range(2):
#     texto = str(input('Digite o texto: '))
#     lista.append(texto)

# for contador in range(len(lista)):
#     if len(lista[contador]) > 5:
#         lista2.append(lista[contador])

# print(lista2)



