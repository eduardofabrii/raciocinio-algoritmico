# Solicitar ao usuário o número de pratos
num_pratos = int(input("Quantos pratos você deseja registrar? "))

# Variáveis para acumular a soma dos pesos e contar pratos acima de 800 gramas
soma_pesos = 0
contagem_acima_800 = 0

# Receber o peso de cada prato do usuário e acumular a soma
for i in range(num_pratos):
    peso = float(input(f"Digite o peso do prato {i + 1} em gramas: "))
    soma_pesos += peso  # Adiciona o peso à soma total
    if peso > 800:  # Verifica se o peso é maior que 800 gramas
        contagem_acima_800 += 1  # Incrementa a contagem

# Calcular o peso médio em gramas
peso_medio = soma_pesos / num_pratos

# Imprimir o resultado
print(f"O peso médio dos pratos é: {peso_medio:.2f} gramas")
print(f"Número de pratos com peso maior que 800 gramas: {contagem_acima_800}")