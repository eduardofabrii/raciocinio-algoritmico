# Calculando carga de caminhão
print('='*35)
caixas_transportadas = int(input('Quantas caixas o caminhão irá transportar? '))
livros_caixas_transportados = int(input('Quantos livros o caminhão vai levar? '))
peso_livros = float(input('Qual peso de cada livro em KG? '))

total_livros_transportados = caixas_transportadas * livros_caixas_transportados
carga = peso_livros * livros_caixas_transportados

print(f'\nO caminhão vai levar {total_livros_transportados} livros\nA carga transportada será de {carga}kg')
print('='*35)

