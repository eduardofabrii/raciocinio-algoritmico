# Verificando se a pessoa pode dirigir
print('='*55)
idade = int(input('Quantos anos você tem? '))
meses_faltante = 216 - (idade * 12)
anos_faltantes = int(meses_faltante / 12)

if idade >= 18:
    print('Você pode tirar a carteira de motorista!')
if idade < 18:
    print(f'Você ainda não pode tirar a carteira de motorista.\nMas poderá tirar a carteira em {meses_faltante} meses ou em {anos_faltantes} ano(s).')
print('='*55)