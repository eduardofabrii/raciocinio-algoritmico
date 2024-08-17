# 1) O número de telefone típico da região de Curitiba recebe o código
# de área 41. Dado um vetor contendo um número de telefone (apenas
# números), criar um algoritmo que inspecione o vetor e imprima na tela
# se o número começa com 41.
# • Exemplo de um telefone da região de Curitiba: 41-9999-8888
lista = []

for linhas in range(1):
    linha = []
    for colunas in range(1):
        telefoneDDD = input('Digite o DDD [41]: ')
        telefone = input('Digite o telefone: ')
        linha.append(telefoneDDD)
        linha.append(telefone)
    lista.append(linha)
    
print(lista)
if lista[0][0] == "41":
    print("O número começa com 41")
else:
    print("O número não começa com 41")