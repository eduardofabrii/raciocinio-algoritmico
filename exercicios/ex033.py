# Um desenvolvedor é conhecido como “Mister
# Digitação”, pois digita muito rapidamente os textos
# utilizando o teclado. Implemente um programa em
# Python para calcular e imprimir na tela a quantidade
# de páginas que ele consegue digitar por hora. O
# programa deve ler a quantidade de caracteres
# digitados em um minuto. Cada página de texto tem
# 1.000 caracteres.

caracteresDigitados = int(input('Indique a quantidade de caracteres digitados por minuto: '))

caracteresPorHora = caracteresDigitados * 60
paginas = caracteresPorHora / 1000
print(f'Quantidade de caracteres digirados por hora: {paginas}')

