times = ['Athletico', 'Bahia', 'Flamengo',
 'Botafogo', 'Sao Paulo', 'Cruzeiro', 'Atletico',
  'Bragantino', 'Palmeiras', 'Internacional', 'Fortaleza',
   'Gremio', 'Vasco', 'Criciuma', 'Juventude', 'Corinthians',
    'Fluminense', 'Vitoria' ,'Atletico-GO', 'Cuiaba']

print('Lista de todos os times do Brasileirão:')
for todos in range(len(times)):
    print(times[todos])
print('Fim da lista')

print('Lista dos 5°:')
print(times[0:5])

print('Lista dos 4 últimos:')
print(times[-4:])

print('Lista em Ordem Alfabética')
print(sorted(times))

cont = 0
print('Flamengo')
print(f'{times.index('Flamengo')+1}°')
