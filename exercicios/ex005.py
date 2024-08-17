# Calculando valor de aluguel de carros
print('='*65)
print('Vamos calcular o valor do aluguel de carros')
print('\nO valor do aluguel de cada carro é R$100,00\nUm único caro pode ser alugado por vários dias (indefinidos)\n')
carros = int(input('Quantos CARROS o cliente alugou? '))
dias = int(input('Quantos DIAS o cliente alugou os CARROS? '))
custo = carros * 100
print(f'Se o cliente alugou {carros} carros por {dias} dias, ele deve pagar {custo}')
print('='*65)