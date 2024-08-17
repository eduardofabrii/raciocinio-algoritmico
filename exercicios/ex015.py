# Calculando quantidade de latas e custo de tanques cilindricos #
print('Vou te ajudar a calcular a quantidade de latas de tinta e o custo para pintar tanques cilindricos.')

altura = float(input('Informe a ALTURA do cilindro em METROS: '))
raio = float(input('Informe o RAIO do cilindro em METROS: '))

area_base = (3.14 * raio * raio)
area_lateral = 2 * 3.14 * raio * altura
area_cilindro = area_base + area_lateral

quantidade_litros = area_cilindro / 3
quantidade_latas = quantidade_litros / 5
custo = quantidade_latas * 50.00

print(f'O custo será de R${custo}. Será necessário comprar {quantidade_latas:.2f} latas de 5L de tinta, que dará {quantidade_litros}L.')