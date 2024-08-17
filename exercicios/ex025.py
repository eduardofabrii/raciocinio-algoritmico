# Implemente um programa em Python para ler 10 inteiros do teclado. Imprima cada número lido na tela, desde que o mesmo seja positivo. Dica: você vai precisar utilizar o for e o if neste 

for cont in range(1, 11, 1):
    numero = int(input('Digite um número: '))
    if numero > 0:
        print(numero)