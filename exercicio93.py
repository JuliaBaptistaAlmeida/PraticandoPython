'''Jogador de Futebol'''

dados = {}
lista = []

c = 1

dados['Nome'] = str(input('Nome do Jogador: '))
dados['Partidas'] = int(input(f'Quantas partidas {dados['Nome']} jogou? '))

for j in range (dados['Partidas']):
    lista.append(int(input(f'Quantos gols {dados['Nome']} fez na partida {c}? ')))
    c += 1

dados['Gols por Partidas'] = lista[:]
dados['Total de Gols'] = sum(lista)

print()
print('==' * 20)
print()
print(dados)
print()
print('==' * 20)
print()

print(f'O jogador {dados['Nome']} jogou {dados['Partidas']} partidas:')
for i, v in enumerate(dados['Gols por Partidas'], 1):
    print(f'=> Na partida {i} ele fez {v} gols.')
print(f'Foi um total de {dados['Total de Gols']} gols.')
