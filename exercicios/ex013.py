# Calculando imposto de renda (valores não atualizados)
renda = float(input('Indique a renda: R$'))

if renda >= 1257.13:
    desconto = (renda * 15) / 100
    print(f'Deverá ser pago R${desconto:.2f} devido salário de R${renda}.')
elif renda >= 2512.08:
    desconto = (renda * 27.5) / 100
    print(f'Deverá ser pago R${desconto:.2f} devido salário de R${renda}.')
else:
    print('Não há valores a serem pagos.')

