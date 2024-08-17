numeroSecreto = float(input('Digite um número SECRETO de 1 a 100: '))
numeroChute = float(input('Adivinhe o número de 1 a 100: '))

while numeroChute != numeroSecreto:
    if numeroChute < numeroSecreto:
        print('O número secreto é maior.')
        numeroChute = float(input('Tente novamente: '))
    elif numeroChute > numeroSecreto:
        print('O número secreto é menor.')
        numeroChute = float(input('Tente novamente: '))
else:
    print('Você acertou, o numero era', numeroSecreto)