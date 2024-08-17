# Implemente um programa em Python para criptografar palavras (lidas pelo
# teclado) utilizando a seguinte estratégia: cada letra da palavra original será
# modificada por outra letra, como segue:
# Original Criptografia
# A D
# B E
# C F
# D G
# E H
# ...
# X A
# Y B
# Z C
# • Imprimir na tela a palavra criptografada

# Crie uma matriz (pode ser 3x3, 4x4, ou outro tamanho à sua escolha).
# Preencha a matriz com números inteiros.
# Calcule a soma de todos os elementos da matriz.
# Imprima a matriz e a soma calculada.

matriz = []

for linhas in range(3):
    linha = []
    for colunas in range(3):
        numeros = int(input(f'Numero ({linhas}, {colunas}): '))
        linha.append(numeros)
    matriz.append(linha)

soma = 0
for linhas in range(3):
    for colunas in range(3):
        soma = soma + matriz[linhas][colunas]

print(matriz)
print(soma)

def criptografando(texto):
    texto = texto.lower()
    cripto_texto = ''
    
    for letra in texto:
        
        if letra == 'a':
            cripto_texto += 'd'
        if letra == 'e':
            cripto_texto += 'h'
        if letra == 'i':
            cripto_texto += 'l'
        if letra == 'o':
            cripto_texto += 'r'
        if letra == 'u':
            cripto_texto += 't'
        
    return cripto_texto

frase = input('Digite uma frase: ')
print(criptografando(frase))