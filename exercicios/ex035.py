# Escreva um programa em Python capaz de ler o valor de um produto
# e imprimir na tela o mesmo para pagamento em três parcelas. O valor
# de um produto tem que ser sempre positivo. Caso não seja, o valor
# deve ser lido novamente.

parcelas = 3
valorProduto = float(input('Indique o valor do produto: R$:'))

if valorProduto < 0:
    print('Tente novamente.')
    valorProduto = float(input('Indique o valor do produto: R$:'))
else:
    valorProduto = valorProduto / parcelas
    print(f'''
    1° Parcela - {valorProduto}
    2° Parcela - {valorProduto}
    3° Parcela - {valorProduto}''')