'''Dicionário em Python'''

dados = {}

dados['Aluno'] = str(input('Nome do aluno: '))
dados['Média'] = float(input(f'Média de {dados['Aluno']}: '))

if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
