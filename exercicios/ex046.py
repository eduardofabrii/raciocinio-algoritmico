# Implemente um programa em Python que seja capaz de criar uma
# string e imprimir na tela:
# • quantas vezes foram encontradas as letras vogais;
# • quantos espaços existem no texto.

contVogal = 0
contEspaco = 0

texto = str(input('Digite o texto: '))
# Paraiso disse que len conta os dados que tem dentro do vetor.
# Range (varra) dentro do tamanho (len) que tem debtro de texto(var).
for vogal in range(len(texto)):
    # "" é vetor de caracteres
    if texto[vogal] == "a" or texto[vogal] == "e" or texto[vogal] == "i" or texto[vogal] == "o" or texto[vogal] == "u":
        contVogal = contVogal + 1
    if texto[vogal] == ' ':
        contEspaco = contEspaco + 1
        
print(f'Vogais encontradas: {contVogal}')
print(f'Espaços encontrados: {contEspaco}')