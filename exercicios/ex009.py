# Calculando média e verificando se aluno está aprovado
print('='*30)
nota_port = float(input('Digite a nota de Português: '))
nota_mat = float(input('Digite a nota de Matemática: '))
nota_hist = float(input('Digite a nota de História: '))
nota_geo = float(input('Digite a nota de Geografia: '))
nota_fis = float(input('Digite a nota de Física: '))
nota_quim = float(input('Digite a nota de Química: '))

media = (nota_port + nota_mat + nota_hist + nota_geo + nota_fis + nota_quim) / 6

# Média será de 6
if media >= 6:
    print('O aluno está aprovado com media', media)
else:
    print('O aluno está reprovado com media', media)
print('='*30)