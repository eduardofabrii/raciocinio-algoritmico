# Calculando valor para entradas de cinema e ticket de esctacionamento
print('='*55)
valor_ingresso = 10
entradas = int(input('Quantas entradas você deseja? '))
carteira_fidelidade = float(input('Indique a porcentagem de desconto da sua carteira: '))
ticket_estacionamento = float(input('Indique o valor do estacionamento: '))

desconto = (entradas * valor_ingresso) - ((valor_ingresso * entradas * carteira_fidelidade) / 100) + ticket_estacionamento

print(f'Valor total = {desconto}')
print('='*55)