# O tempo de voo entre São Paulo e Curitiba pode variar em função de
# diversos fatores. Dentre eles, está a velocidade máxima atingida pelo
# avião que faz o transporte. O gerente de uma empresa de táxi aéreo
# gostaria de saber o tempo médio de viagens feitas neste trecho. Para
# tal, ele te contratou para escrever um programa em Python capaz de
# ler o tempo gasto no trecho para cada tipo de avião. A empresa tem 3
# tipos diferentes de aviões: “pequenos”, “médios” e “grandes”. O
# cálculo será feito para 10 viagens no total. Ao final, imprimir na tela o
# tempo médio gasto para o trecho, por tipo

aviaoPequeno = 0
aviaoMedio = 0
aviaoGrande = 0

for distancia in range(10):
    velocidadePequeno = float(input('Diga a velocidade máxima do avião Pequeno: '))
    velocidadeMedio = float(input('Diga a velocidade máxima do avião Medio: '))
    velocidadeGrande = float(input('Diga a velocidade máxima do avião Grande: '))

aviaoPequeno = aviaoPequeno + velocidadePequeno
aviaoMedio = aviaoMedio + velocidadeMedio
aviaoGrande = aviaoGrande + velocidadeGrande

print(f'A velocidade média do avião pequeno é de {aviaoPequeno}')
print(f'A velocidade média do avião medio é de {aviaoMedio}')
print(f'A velocidade média do avião grande é de {aviaoGrande}')

# cont_grande = 0
# tempo_medio_grande = 0
# cont_medio = 0
# tempo_medio_medio = 0
# cont_pequeno = 0
# tempo_medio_pequeno = 0

# for cont_viagens in range(10):
#     print("1 - Aviao Grande")
#     print("2 - Aviao Medio")
#     print("3 - Aviao Pequeno")
#     escolha = int(input("Digite o tipo de aviao = "))
#     tempo_viagem = int(input("Digite o tempo em min = "))
#     if escolha == 1:
#         tempo_medio_grande = tempo_medio_grande + tempo_viagem
#         cont_grande = cont_grande + 1
#     elif escolha == 2:
#         tempo_medio_medio = tempo_medio_medio + tempo_viagem
#         cont_medio = cont_medio + 1
#     elif escolha == 3:
#         tempo_medio_pequeno = tempo_medio_pequeno + tempo_viagem
#         cont_pequeno = cont_pequeno + 1
#     else:
#         print("Escolha inválida")
#     if cont_grande > 0:
#         media_grande = tempo_medio_grande/cont_grande
#         print("Tempo medio grande = ", media_grande)
#     else:
#         print("Nenhum trecho com aviao grande")
#     if cont_medio > 0:
#         media_medio = tempo_medio_medio/cont_medio
#         print("Tempo medio medio = ", media_medio)
#     else:
#         print("Nenhum trecho com aviao medio")
#     if cont_pequeno > 0:
#         media_pequeno = tempo_medio_pequeno/cont_pequeno
#         print("Tempo medio pequeno = ", media_pequeno)
#     else:
#         print("Nenhum trecho com aviao pequeno")
