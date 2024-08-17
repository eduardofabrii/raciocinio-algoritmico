# Maneira errada
# def validar_numero(numero, menor, maior):
#     if numero > menor and numero < maior:
#         return True
#     else:
#         return False

# menor = float(input('Digite o menor número possivel: '))
# maior = float(input('Digite o maior número possivel: '))
# numero = float(input('Digite um número: '))
# print(validar_numero(numero, menor, maior))

#  Maneira correta!
def validar_numero(numero, menor, maior):
    if numero > menor and numero < maior:
        return True
    else:
        return False

menor = float(input('Digite o menor número possivel: '))
maior = float(input('Digite o maior número possivel: '))
numero = float(input('Digite um número: '))

resultado = (numero, menor, maior)
print(resultado)

if resultado == menor:
    print(f'O número {numero} é invalido pois é maior que {maior}.')
else:
    print(f'O número {numero} é valido pois é maior que {menor}.')

