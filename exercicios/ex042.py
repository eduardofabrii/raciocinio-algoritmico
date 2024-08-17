# • 2) Implemente um programa em Python para verificar quantos números uma
# aposta acertou na Megasena. O programa deve ler do teclado os 6 números
# sorteados e comparar com 6 números apostados.
# • Obs: utilizar comparação posição a posição dos vetores. 
            # Utilizei a OBS mas resolvi implementar a função sort para nao deixar posição a posição

# quantidade = 0
# listaSorteados = []
# listaApostados = []

# print('='*20, 'Números Sorteados', '='*20)
# for contador in range(6):
#     numerosSorteados = int(input('Indique os números sorteados: '))
#     listaSorteados.append(numerosSorteados)
#     listaSorteados.sort()

# print('='*20, 'Números Apostados', '='*20)
# for contador in range(6):
#     numerosApostados = int(input('Indique os números apostados: '))
#     listaApostados.append(numerosApostados)
#     listaApostados.sort()

# print('='*20, 'Quantidade de acertos', '='*20)
# for contador in range(6):
#     if listaApostados[contador] == listaSorteados[contador]:
#         quantidade = quantidade + 1

# print('Quantidade de acertos: ', quantidade)
# print('='*63)




# acertos = 0
# listaSorteados = []
# listaApostados = []

# for contador in range(6):
#     numeroSorteado = int(input('Digite o número sorteado: '))
#     listaSorteados.append(numeroSorteado)

# for contador in range(6):
#     numeroApostado = int(input('Digite o número apostado: '))
#     listaApostados.append(numeroApostado)

# for contador in range(6):
#     if listaSorteados[contador] == listaApostados[contador]:
#         acertos = acertos + 1
#     else:
#         print(f'Você errou.')

# print(f'Acertos: {acertos}')

from random import randint

numeros_sorteio = []
numeros_aposta = []

for _ in range(6):
    numero = randint(1, 60)
    numeros_sorteio.append(numero)

print("\nInsira os números da sua aposta:")

for i in range(6):
    numero = int(input(f"Número {i+1}: "))
    numeros_aposta.append(numero)

print(numeros_sorteio)
print(numeros_aposta)
if numeros_aposta == numeros_sorteio:
    print('Parabéns, você é o novo milionário')
else:
    print('Que pena, continue tentando')
contador = 0

# # Apenas para encher linguiça 
# for c in range(len(numeros_sorteio)):
#     for c in range(len(numeros_aposta)):
#         if numeros_aposta == numeros_sorteio:
#             contador +=1
# print('Valores em comum:', contador)
