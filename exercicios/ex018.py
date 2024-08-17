# Verificando se a nota é um valor válido ou não
nota = float(input('Insira a nota: '))

while nota < 0:
        print('Nota invalida')
        nota = float(input('Insira a nota: '))
else:
    print('A nota é válida.')

# Outra maneira
# nota = float(input("Digite a nota (entre 0 e 10) = "))

# while nota < 0 or nota > 10:
#     print("Nota invalida. Digite novamente.")
# nota = float(input("Digite a nota (entre 0 e 10) = "))