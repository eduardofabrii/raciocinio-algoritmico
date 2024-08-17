# Implemente uma calculadora em Python capaz de realizar as
# seguintes operações elementares envolvendo inteiros:
# • Somar dois valores;
# • Dividir dois valores;
# • Multiplicar dois valores;
# • Subtrair dois valores;
# • Todos os resultados devem ser impressos na tela (fora do módulo);
# • Utilizar passagem de parâmetros e retorno.

def somar(a, b):
    soma = a + b
    return soma

def subtrair(a, b):
    subtracao = a - b
    return subtracao

def multiplicar(a, b):
    multiplicacao = a * b
    return multiplicacao

def dividir(a, b):
    divisao = a / b
    return divisao



def printarCalculadora(valor1, valor2):
    print(f'O calculo {valor1} + {valor2} = {somar(valor1, valor2)}')
    print(f'O calculo {valor1} - {valor2} = {subtrair(valor1, valor2)}')
    print(f'O calculo {valor1} * {valor2} = {multiplicar(valor1, valor2)}')
    print(f'O calculo {valor1} / {valor2} = {dividir(valor1, valor2):.2f}')
    return valor1, valor2

def escolherOperacao(valor1, valor2, escolha):
    if escolha == 1:
        print(f'O calculo {valor1} + {valor2} = {somar(valor1, valor2)}')
    elif escolha == 2:
        print(f'O calculo {valor1} - {valor2} = {subtrair(valor1, valor2)}')
    elif escolha == 3:
        print(f'O calculo {valor1} * {valor2} = {multiplicar(valor1, valor2)}')
    elif escolha == 4:
        print(f'O calculo {valor1} / {valor2} = {dividir(valor1, valor2):.2f}')
    elif escolha == 5:
        resultadoCalculadora = printarCalculadora(valor1, valor2) # ou usar - return printarCalculadora(valor1, valor2)
    else:
        print('Escolha incorreta.')
    return valor1, valor2, escolha

valor1 = float(input('Digite um número: '))
valor2 = float(input('Digite outro número: '))
print('[1] - SOMAR')
print('[2] - SUBTRAIR')
print('[3] - MULTIPLICAR')
print('[4] - DIVIDIR')
print('[5] - TODOS')
escolha = int(input('Escolha um número de opção: '))
chamar = escolherOperacao(valor1, valor2, escolha)












