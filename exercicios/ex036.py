# Um professor quando corrige suas provas atribui uma nota de 0 a 100. Ocorre
# que a escola onde trabalha este professor divulga as notas aos alunos sob a forma
# de conceitos, como apresentado na tabela abaixo:
# • Você deve escrever um programa em Python que recebe uma nota no sistema
# numérico e determina (imprime na tela) o conceito correspondente.

nota = float(input('Digite a nota: '))

if nota == 0:
    print('Nota E')
elif nota >= 1 and nota <= 35:
    print('Nota D')
elif nota >= 36 and nota <= 60:
    print('Nota C')
elif nota >= 61 and nota <= 85:
    print('Nota B')
elif nota >= 86 and nota <= 100:
    print('Nota A')
else:
    print('Nota Inválida.')