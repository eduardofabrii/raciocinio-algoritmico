# Em uma competição de saltos ornamentais são obtidas dos jurados 7
# notas, onde são eliminadas a nota maior e a nota menor, e a
# valoração do salto é feita pela soma das demais notas. Crie um
# programa que recebe as notas dos juízes, remove a maior e menor
# nota e soma as demais fazendo uso de métodos de listas e funções
# Built in.

def fatorial(numero):
    if numero > 0:
        return numero * fatorial(numero - 1)
    return 1

numero = int(input('Digite um número: '))
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}.')