# Calculando horas transcorridas
print('='*50)
horas = int(input('Indique que HORAS são: '))
minutos = int(input('Digite quantos MINUTOS são: '))
horas_apos = int(input('Indique que HORAS são: '))
minutos_apos = int(input('Digite quantos MINUTOS são: '))
horas_transcorridas = horas_apos - horas
minutos_transcorridos = minutos_apos - minutos
print(f'Passaram {horas_transcorridas}h e {minutos_transcorridos}min.')
print('='*50)
# Tem alguns erros

# Para calcular minutos transcorridos
print('='*50)
hora_inicial = int(input("Digite a hora inicial = "))
minuto_inicial = int(input("Digite o minuto inicial = "))
hora_final = int(input("Digite a hora final = "))
minuto_final = int(input("Digite o minuto final = "))
hora_inicial_transcorrido = hora_inicial*60 + minuto_inicial
hora_final_transcorrido = hora_final*60 + minuto_final
diferenca = hora_final_transcorrido - hora_inicial_transcorrido
print("Minutos transcorridos = ", diferenca)
print('='*50)