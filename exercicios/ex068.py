def criptografar(texto):
    novoTexto = ''
    for cont in range(len(texto)):
        if texto[cont] >= chr(97) and texto[cont] <= chr(97 + 22):
            novoTexto += chr(ord(texto[cont]) + 3)
        else:
            if texto[cont] == chr(97 + 23):
                novoTexto += 'a'
            else:
                if texto[cont] == chr(97 + 24):
                    novoTexto += 'b'
                else:
                    if texto[cont] == chr(97 + 25):
                        novoTexto += 'c'
                    else:
                        novoTexto += texto[cont]
    return novoTexto

texto = input('Digite o texto: ')        
novoTexto = criptografar(texto)
print(novoTexto)