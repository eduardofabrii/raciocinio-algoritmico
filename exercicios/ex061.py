#  1) Um vendedor de carros está com dificuldade em calcular sua comissão a cada
# venda que realiza. Você irá ajudá-lo implementado um programa capaz de, dado
# o valor da venda (valor do carro) e o percentual da comissão, indicar quanto o
# vendedor ganhará.
# • Exemplo:
# • Valor da venda: 50.000,00 reais
# • Comissão: 3%
# • Ganho do vendedor: 1.500,00 reais
# • PS: Obrigatório uso de função neste programa

def ganhos_vendedor(valor_venda, valor_comissao):
    calculo = (valor_venda * valor_comissao / 100)
    return calculo

valorVenda = float(input('Digite o valor da venda do carro: '))
valorComissao = float(input('Digite o da comissão da venda do carro: '))

resultado = ganhos_vendedor(valorVenda, valorComissao)
print(f'O ganho do vendedor é de R${resultado}.')