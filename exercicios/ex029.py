# Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto Felisberto tem 1,10 metro e cresce 3 centímetros por ano. Construa um algoritmo em Python que calcule e mostre quantos anos serão necessários para que Felisberto seja maior que Anacleto.

anacleto = 150
felisberto = 110
contador = 0

while felisberto < anacleto:
    anacleto = anacleto + 2
    felisberto = felisberto + 3
    contador = contador + 1
    
print(f'Serão necessários {contador} anos.')