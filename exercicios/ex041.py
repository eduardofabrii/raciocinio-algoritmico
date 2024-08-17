# 1) Dado um vetor de inteiros de 10 posições lido pelo teclado, 
# desenvolver um programa para localizar e
#  imprimir na tela a posição de um elemento qualquer, digitado pelo usuário. 
# Caso o elemento não esteja armazenado no vetor, imprimir "Não está no vetor".

lista = []

for contador in range(10):
    posicoes = int(input(f'Insira a {contador+0}° posição:  '))
    lista.append(posicoes)

procura = int(input('Qual elemento você procura? '))

if lista.count(procura) == 0:
    # O 0 serve para quando o elemento não é encontrado, faz a varredura da lista
    print('Não está na lista.')
else:
    print(f'O elemento esta na {lista.index(procura)}° posição.')
    print(f'Existem {lista.count(procura)} número(s) {procura} na lista.')
    
