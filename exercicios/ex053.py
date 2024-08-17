numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

conversao = int(input('Digite um número entre 0 e 20: '))

while conversao >= 0:
    if conversao < 0 or conversao > 20:
        conversao = int(input('Tente novamente: '))
    else:
        print(f'Você digitou o número {numeros[conversao]}')
        break
