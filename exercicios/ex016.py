# Verificando se os comprimentos podem ser lados de um triangulo e qual triangulo pertence
valor_a = float(input('Digite o 1° valor do triângulo: '))
valor_b = float(input('Digite o 2° valor do triângulo: '))
valor_c = float(input('Digite o 3° valor do triângulo: '))

if (valor_a <= valor_b + valor_c and valor_a + valor_c and valor_c <= valor_a + valor_b):
    print('Forma um triângulo.')
    
    if valor_a == valor_b == valor_c:
        print('O triângulo é equilátero.')

    elif valor_a == valor_b or valor_a == valor_c or valor_b == valor_c:
        print('O triângulo é isósceles.')

    else:
        print('O triângulo é escaleno.')

else:
    print('Não será possivel formar um triângulo')



