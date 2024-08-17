for contador in range(10):
    numero = int(input('Insira um número: '))
    resto = numero % 2
    if resto == 0:
        print('O numero é par.')
    else:
        print('O numero é impar.')