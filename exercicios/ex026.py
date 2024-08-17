# Implemente um algoritmo que leia um inteiro e calcule o seu fatorial. Dica: o fatorial de 5 é 120, obtido como: 5! = 5 * 4 * 3 * 2 * 1.

numero = int(input('Digite um número: '))
cont = numero
fatorial = 1

while cont > 0:
    print(cont)
    fatorial = fatorial * cont
    cont = cont - 1

print(fatorial)