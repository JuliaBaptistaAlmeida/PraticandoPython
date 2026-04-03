'''Carteira de Trabalho'''

from datetime import date

dados = {}

dados['Nome'] = str(input('Digite o nome: '))
nasc = int(input(f'Digite o ano de nascimento de {dados['Nome']}: '))
ano = date.today().year
dados['Idade'] = ano - nasc
dados['Carteira'] = int((input(f'Carteira de Trabalho (ou 0 se não tiver): ')))

if dados['Carteira'] > 0:
    dados['Contratação'] = int(input('Digite o ano da primeira contratação: '))
    dados['Salário'] = int(input('Salário atual: R$ '))
    dados['Aposentadoria'] = (dados['Idade'] + dados['Contratação'] + 35) - ano

print('==' * 16)

for k, v in dados.items():
    print(f'{k} é igual a {v}.')
