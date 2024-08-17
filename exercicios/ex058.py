def calcular_consumo():
    litros = float(input("Digite a Quant. de litros consumidos: "))
    quilometros = float(input("Digite a Quantidade de km rodados: "))
    if litros > 0:
        consumo = quilometros/litros
    else:
        return False # Tratamento de erro
    return consumo

print("Consumo =", calcular_consumo(), "km/l") 
# Jeito errado, é melhor criar uma variavel com a função

while True:
    consumo = calcular_consumo()
    if consumo == False: # Tratamento de erro
        print("Valor inválido. Tente novamente.")
    else:
        print("Consumo =", consumo, "km/l")
        break