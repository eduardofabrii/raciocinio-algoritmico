# Criar um programa que solicite o nome de 4 times de futebol. O
# programa deve simular partidas de forma que cada time jogue uma
# vez com os outros 3 times. Na partida deve perguntar quantos gols
# fez cada time, e somar as devidas pontuações. Ao final deve dizer
# qual ou quais times foram campeões, uma vez que pode haver
# empate em pontuação. Obs.: vitória vale 3 pontos para o vencedor,
# empate vale 1 ponto para cada time e derrota não soma pontos.
teams = []
points = {}

# Solicitar o nome dos 4 times
for i in range(4):
    team_name = input("Digite o nome do time: ")
    teams.append(team_name)
    points[team_name] = 0

# Simular as partidas
for i in range(4):
    for j in range(i+1, 4):
        team1 = teams[i]
        team2 = teams[j]
        goals1 = int(input(f"Quantos gols o time {team1} fez contra o time {team2}? "))
        goals2 = int(input(f"Quantos gols o time {team2} fez contra o time {team1}? "))

        if goals1 > goals2:
            points[team1] += 3
        elif goals1 < goals2:
            points[team2] += 3
        else:
            points[team1] += 1
            points[team2] += 1

champion_teams = []
# Encontrar o(s) time(s) campeão(ões)
for i in range(len(teams)):
    for j in range(len(teams)):

        


for team, score in points.items():
    if score == max_points:
        champion_teams.append(team)

# Imprimir o(s) time(s) campeão(ões)
print("Time(s) campeão(ões):")
for team in champion_teams:
    print(team)
    # Verificar se houve empate
    if len(champion_teams) > 1:
        print("Houve empate entre os seguintes times:")
        for team in champion_teams:
            print(team)
    else:
        print("O time campeão é:")
        print(champion_teams[0])
