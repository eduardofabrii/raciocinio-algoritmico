m = "m"
f = "f"
sexo = str(input('Diga se você é Mulher (F) ou Homem (M): '))

while sexo != m and sexo != f:
    sexo = str(input('Diga se você é Mulher (F) ou Homem (M): '))
else:
    print('Ok.')
    