valores = []
for cont in range(0, 5):
    numero = int(input('Digite um número: '))
    valores.append(numero)

for linha in range(len(valores)):
    coluna = valores[linha]
    print(f'Na linha {linha+1} encontrei o valor {coluna}')

