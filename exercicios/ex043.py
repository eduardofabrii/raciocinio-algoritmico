
# • 3) Um armazém trabalha com 100 mercadorias diferentes identificadas pelos
# números inteiros de 1 a 100. O dono do armazém anota a quantidade de cada
# mercadoria vendida durante o mês. Ele tem uma tabela que indica para cada
# mercadoria o preço de venda. Escreva o algoritmo para calcular o faturamento
# mensal do armazém, isto é:
# • faturamento = Quantidade * preço

# faturamento = 0
# ticketMedio = 0
# tabelaVendidas = []
# tabelaPreco = []

# for tabela in range(2):
#     print('\n','='*22, f'Mercadoria {tabela+1}', '='*22, '\n')
#     quantidadeMercadoria = int(input(f'Indique a quantidade da mercadoria {tabela+1} vendida no mês: '))
#     tabelaVendidas.append(quantidadeMercadoria)
#     precoMercadoria = float(input(f'Indique o valor da mercadoria {tabela+1}: R$'))
#     tabelaPreco.append(precoMercadoria)

# for tabela in range(len(tabelaVendidas)):
#     faturamento = faturamento + (tabelaVendidas[tabela] * tabelaPreco[tabela])
#     ticketMedio = faturamento / tabelaVendidas[tabela]

# print(f'Faturamento Mensal = R$ {faturamento:.2f}')
# print(f'Ticket Médio = R$ {ticketMedio:.2f}')

precoMercadoria = []
quantidadeVendas = []
faturamento = 0

for contador in range(2):
    precoProduto = float(input(f'Digite o preço do produto {contador+1}: R$'))
    precoMercadoria.append(precoProduto)
    vendas = int(input('Indique quantas vendas foram feitas desse produto: '))
    quantidadeVendas.append(vendas)

faturamento = faturamento + (precoMercadoria[contador] * quantidadeVendas[contador])
print(faturamento)

