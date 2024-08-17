# 2) Um vetor contém o salário mensal de uma pessoa, durante um ano.
# Implemente um programa em Python para:
# • Imprimir a média de salário recebido;
# • imprimir na tela os valores abaixo da média contidos no vetor.

salarios = [1000, 1500, 2000, 2500,
3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]

soma = 0
for contador in range(len(salarios)):
    soma += salarios[contador]

media = soma / len(salarios)
print("Média de salário recebido:", media)

print("Valores abaixo da média:")
for contador in range(len(salarios)):
    if salarios[contador] < media:
        print(salarios[contador])