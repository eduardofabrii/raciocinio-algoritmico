
# Verificando categoria de um lutador
print('Vamos verificar qual CATEGORIA o lutador se encaixa:')
peso = float(input('Insira o peso do lutador em kg: '))

if peso < 50:
    print('Peso Palha')
elif peso <= 60:
    print('Peso Pluma')
elif peso <= 76:
    print('Peso Leve')
elif peso <= 88:
    print('Peso Pesado')
else:
    print('Peso Super Pesado')