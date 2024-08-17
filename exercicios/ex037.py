# Teste para média de aluno e lista

listaNotas = []


for cont in range(5):
    nota = float(input(f'Digite a nota {cont+1}: '))
    listaNotas.append(nota)

for cont in range(5):
    print(listaNotas[cont])

soma = 0
for cont in range(5):
    soma = soma + listaNotas[cont]

media = soma / 5
print('Média:', media)

for cont in range(5):
    if listaNotas[cont] > media:
        print(listaNotas[cont])