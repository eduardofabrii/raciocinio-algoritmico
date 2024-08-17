# Descubra como calcular o IMC (Índice de Massa Corporal) e crie uma função para retornar o IMC de uma pessoa.

def calcular_imc(peso, altura):
    if peso > 0 and altura > 0:
        imc = peso / (altura * altura)
        return imc

    return False

peso = float(input('Indique o peso: '))
altura = float(input('Indique a altura: '))

teste = calcular_imc(peso, altura)
if teste != False:
    print(f'IMC: {teste:.2f}')
else:
    print('Incorreto.')
