soma = 0
contador = 0

while contador < 10:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma += numero
    contador += 1

print("A soma dos números informados é:", soma)
