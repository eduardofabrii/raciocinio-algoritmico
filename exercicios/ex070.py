# A partir de uma string lida pelo teclado, como você faria para contar
# o número de palavras presentes na string? Implemente a solução em
# uma função que recebe a string e retorna a quantidade de palavras. 


def contar_palavras(texto):
    contEspaco = 0
    for contar in range(len(texto)):
        if texto[contar] == ' ':
            contEspaco = contEspaco + 1
    palavras = contEspaco + 1
    return palavras

string_lida = str(input('Digite o texto: '))
teste = contar_palavras(string_lida)
print(teste)