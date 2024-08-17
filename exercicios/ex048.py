# Crie uma matriz de notas para 3 alunos com 4 notas cada.
# Depois imprima na tela a média individual de cada aluno.

notas = []

for linhas in range(3):
    linha = []
    # linhas.append(aluno) 
    # notas.append(aluno) # Essa linha funciona para deixar ['e', 1, 2, 3, 4]
    # linhas.append(aluno) # Essa linha funciona para deixar ['e', 1, 2, 3, 4]
    for colunas in range(4):
        notaAluno = float(input(f'Digite a {colunas+1}° nota do aluno {linhas+1}: '))
        linha.append(notaAluno)
    notas.append(linha)    
print(notas)


for linhas in range(3):
    soma = 0
    for colunas in range(4):
        soma = soma + notas[linhas][colunas]
    media = soma / 4
    print(f'O aluno {linhas+1} está com média de {media:.2f}.')

    
        


















# notas = []

# for linha in range(4): #avaliacao
#     linhas = []
#     for coluna in range(2): #alunos
#         notaAluno = float(input(f'Insira a {linha+1}° nota do aluno {coluna+1}: '))
#         linhas.append(notaAluno)
#     notas.append(linhas)
# print(linhas)

# duvida = str(input('Insira "continuar" ou "parar": '))
# if duvida == "continuar": 
#     while duvida == "parar":
#         break
#     else:
#         print('Digite "parar" para sair do programa.')
#         escolha = str(input('Você deseja procurar o aluno ou avaliacao: '))
#         if escolha == "avaliacao":
#             for avaliacoes in range(len(notas)):
#                 print(f'Avaliações: {notas[avaliacoes]}')
#         if escolha == "aluno":
#             for alunos in range(len(notas)):
#                 print(f'Aluno {alunos+1}: {notas[avaliacoes]}')
# else:
#     print('Programa encerrado.')
