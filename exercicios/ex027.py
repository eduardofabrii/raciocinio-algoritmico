# Implemente um algoritmo em Python capaz de ler 5 inteiros do teclado e imprimir na tela o maior número digitado. Dica: você vai precisar utilizar o for e o if neste exercício.

numero = int(input('Digite um número: '))


for cont in range(4):
    maiorNumero = int(input('Digite um número: '))
    if maiorNumero < numero:
        print(maiorNumero)

        #  n funciona