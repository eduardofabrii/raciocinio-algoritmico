# Calculando idade
print('='*70)
ano_nascimento = int(input('Digite o ANO de nascimento: '))
ano_atual = int(input('Digite o ano ATUAL: '))
idade = ano_atual - ano_nascimento
print(f'Se a pessoa nasceu em {ano_nascimento} e estamos em {ano_atual}, então ela tem {idade} anos.')
print('='*70)