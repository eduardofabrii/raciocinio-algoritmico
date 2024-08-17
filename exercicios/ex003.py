# Calculando possiveis faltas em uma matéria
print('='*35)
aulas_totais = int(input('Quantas aulas a matéria tem no semestre? '))
faltas = (aulas_totais * 25) / 100
print(f'Você pode faltar {faltas:.2f} aulas.')
print('='*35)