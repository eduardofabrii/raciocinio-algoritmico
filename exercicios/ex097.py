# Implementar um programa contendo um procedimento em
# Python para calcular o valor que deve ser pago por uma
# pessoa que deixa seu carro estacionado por X horas em um
# estacionamento que cobra Y reais por hora. O procedimento
# deve receber os valores X e Y via argumentos.

def calcular_valor_estacionamento(horas, valor_hora):
    valor_total = horas * valor_hora
    return valor_total

horas_estacionadas = 3
valor_por_hora = 10
valor_a_pagar = calcular_valor_estacionamento(horas_estacionadas, valor_por_hora)
print(f"Valor a pagar: R${valor_a_pagar:.2f}")