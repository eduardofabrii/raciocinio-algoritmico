# Implemente um programa em Python para verificar se um número
# passado como argumento para um módulo está em um determinado
# intervalo de valores, também passado como argumento. Se estiver o
# módulo retorna True, senão False.

def checar_intervalo(numero, primeiroNumero, ultimoNumero):
    if numero >= primeiroNumero and numero <= ultimoNumero:
        return True
    else:
        return False

# Example usage
numero = 5
primeiroNumero = 1
ultimoNumero = 10
resultado = checar_intervalo(numero, primeiroNumero, ultimoNumero)
print(resultado)

if resultado:
    print("O número está dentro do intervalo.")
else:
    print("O número está fora do intervalo.")



    