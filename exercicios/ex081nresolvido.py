# Receber a lista de números
numeros = input("Digite os números separados por espaço: ").split()

# Converter os números para inteiros
numeros_inteiros = []
for numero in numeros:
    numeros_inteiros.append(int(numero))

# Ordenar a lista de números
for i in range(len(numeros_inteiros)):
    for j in range(i + 1, len(numeros_inteiros)):
        if numeros_inteiros[i] > numeros_inteiros[j]:
            numeros_inteiros[i], numeros_inteiros[j] = numeros_inteiros[j], numeros_inteiros[i]

# Calcular a mediana
tamanho = len(numeros_inteiros)
if tamanho % 2 == 1:
    mediana = numeros_inteiros[tamanho // 2]
else:
    mediana = (numeros_inteiros[tamanho // 2 - 1] + numeros_inteiros[tamanho // 2]) / 2

# Imprimir a mediana
print("A mediana dos números é:", mediana)
