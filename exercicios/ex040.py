escolha = True
valorUm = float(input('Digite um valor: '))
valorDois = float(input('Digite outro valor: '))

while True:
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    escolha = input('Escolha a opção que deseja: ')

    while escolha:
        if escolha == "1":
            soma = valorUm + valorDois
            print(f'{valorUm} + {valorDois} = {soma}')
            print('[1] - Somar')
            print('[2] - Multiplicar')
            print('[3] - Maior')
            print('[4] - Novos números')
            print('[5] - Sair do programa')
            escolha = input('Escolha a opção que deseja: ')
        if escolha == "2":
            multiplicar = valorUm * valorDois
            print(f'{valorUm} * {valorDois} = {multiplicar}')
            print('[1] - Somar')
            print('[2] - Multiplicar')
            print('[3] - Maior')
            print('[4] - Novos números')
            print('[5] - Sair do programa')
            escolha = input('Escolha a opção que deseja: ')
        if escolha == "3":
            if valorUm > valorDois:
                print(f'{valorUm} > {valorDois}')
                print('[1] - Somar')
                print('[2] - Multiplicar')
                print('[3] - Maior')
                print('[4] - Novos números')
                print('[5] - Sair do programa')
                escolha = input('Escolha a opção que deseja: ')
            elif valorUm < valorDois:
                print(f'{valorUm} < {valorDois}')
                print('[1] - Somar')
                print('[2] - Multiplicar')
                print('[3] - Maior')
                print('[4] - Novos números')
                print('[5] - Sair do programa')
                escolha = input('Escolha a opção que deseja: ')
        if escolha == "4":
            print('Escolha novos números:')
            valorUm = float(input('Digite um valor: '))
            valorDois = float(input('Digite outro valor: '))
            print('[1] - Somar')
            print('[2] - Multiplicar')
            print('[3] - Maior')
            print('[4] - Novos números')
            print('[5] - Sair do programa')
            escolha = input('Escolha a opção que deseja: ')
        if escolha == "5":
            False
        else:
            print('Tente uma opção válida.')
            escolha = input('Escolha a opção que deseja: ')
    else:
        print('Sistema encerrado.')