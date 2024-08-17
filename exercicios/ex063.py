global saldo
saldo = 0

def criar_conta(saldo_inicial):
    global saldo
    saldo = saldo + saldo_inicial

def depositar(deposito):
    global saldo
    saldo += deposito

def retirar(retirando):
    global saldo
    if saldo > 0:
        saldo -= retirando
        return saldo
    else:
        print('Saldo zero.')
        return False

def imprimir_saldo():
    print(f'Saldo: {saldo}')

def menu():
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Retirar")
    print("4 - Imprimir saldo")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        saldo = float(input("Informe o saldo inicial: "))
        c = criar_conta(saldo)
    elif opcao == 2:
        deposito = float(input("Informe o valor do depósito: "))
        d = depositar(deposito)
    elif opcao == 3:
        retirando = float(input("Informe o valor a ser retirado: "))
        r = retirar(retirando)
        if r:
            print("Retire")
    elif opcao == 4:
        imprimir_saldo()
    elif opcao == 5:
        return
    else:
        print("Opção inválida!")

while True: 
    menu()


