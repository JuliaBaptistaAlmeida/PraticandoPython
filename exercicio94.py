'''Unindo dicionários e Listas'''

dados = {}
lista = []
soma = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))

    dados['Sexo'] = str(input('Sexo (F/M): ')).upper().strip()[0]
    while dados['Sexo'] not in 'FM':
        dados['Sexo'] = str(input('Digite F para feminino ou M para masculino: ')).upper().strip()[0]

    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']

    lista.append(dados.copy())

    continuar = str(input('Deseja continuar? (S/N): ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite S para sim ou N para não: ')).upper().strip()[0]
    if continuar == 'N':
        break

print()
print(f'Ao todo, {len(lista)} pessoas foram cadastradas.')
media = soma / len(lista)
print(f'A média das idades é {media:.2f} anos.')

mulheres = [p['Nome'] for p in lista if p['Sexo'] == 'F']
if mulheres:
    print(f'Total de mulheres cadastradas: {len(mulheres)}')
    print(f'Sendo elas: {", ".join(mulheres)}')
else:
    print('Nenhuma mulher foi cadastrada.')

print('\nLista de pessoas com idade acima da média:')
for p in lista:
    if p['Idade'] > media:
        print()
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print() 

print()
