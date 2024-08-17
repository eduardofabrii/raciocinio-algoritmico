#  eerrrradooooo
lista = []
maior = 0
menor = 0


for contador in range(5):
    numeros = float(input('Digite um número: '))
    lista.append(numeros)
    
for numero in range(len(lista)):
    if lista[numero] > maior:
        maior = lista[numero]
print(f'O maior número inserido é: {maior}')

if lista[numero] < menor or menor == 0:
        menor = lista[numero]
print(f'O menor número inserido é: {menor}')