# O tempo de voo entre São Paulo e Curitiba pode variar em função de
# diversos fatores. Dentre eles, está a velocidade máxima atingida pelo
# avião que faz o transporte. O gerente de uma empresa de táxi aéreo
# gostaria de saber o tempo médio de viagens feitas neste trecho. Para
# tal, ele te contratou para escrever um programa em Python capaz de
# ler o tempo gasto no trecho para cada tipo de avião. A empresa tem 3
# tipos diferentes de aviões: “pequenos”, “médios” e “grandes”. O
# cálculo será feito para 10 viagens no total. Ao final, imprimir na tela o
# tempo médio gasto para o trecho, por tipo. 

viagens = 10
totalTempoAviaoPequeno = 0
totalTempoAviaoMedio = 0
totalTempoAviaoGrande = 0

for cont in range(viagens):
    tempoAviaoPequeno = float(input('Indique o tempo gasto no trajeto do avião pequeno: '))
    tempoAviaoMedio = float(input('Indique o tempo gasto no trajeto do avião médio: '))
    tempoAviaoGrande = float(input('Indique o tempo gasto no trajeto do avião grande: '))

totalTempoAviaoPequeno =  totalTempoAviaoPequeno + tempoAviaoPequeno
print(totalTempoAviaoPequeno)

totalTempoAviaoMedio =  totalTempoAviaoMedio + tempoAviaoMedio
print(totalTempoAviaoMedio)

totalTempoAviaoGrande =  totalTempoAviaoGrande + tempoAviaoGrande
print(totalTempoAviaoGrande)



