saque = float(input('Valor do saque: R$'))

while True:
    if saque < 10 and saque > 600:
        print('O saque deve ser maior que R$10,00 e menor que R$600,00.')
        saque = float(input('Valor do saque: R$'))
    elif saque > 10 and saque < 600:
        notasCem = saque // 100
        saque %= 100
        print(f'Notas de R$100,00: {notasCem}')
        notasCinquenta = saque // 50
        saque %= 50
        print(f'Notas de R$50,00: {notasCinquenta}')
        saque %= 10
        print(f'Notas de R$10,00: {notasDez}')
        
    else:
        break

        
