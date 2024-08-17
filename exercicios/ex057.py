# Implemente um algoritmo em Python para permitir a aposta
# de 5 jogadores em um bolão da Copa do Mundo. Cada
# jogador indicará o resultado dos 3 primeiros jogos do Brasil,
# no seguinte formato:
# Jogo 1: 2 x 0
# Jogo 2: 5 x 1
# Jogo 3: 3 x 0

apostas = []

for resultado in range(5):
    linha = []
    for jogos in range(3):
        jogo = str(input(f'Jogador {resultado+1} | Jogo {jogos+1}: '))
        linha.append(jogo)
    apostas.append(linha)

for resultado in range(5):
    print(f'Jogador {resultado+1} apostou:')
    for jogos in range(3):
         print(f'Jogo {jogos+1}: {apostas[resultado][jogos]}')
