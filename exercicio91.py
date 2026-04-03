'''Jogos de Dados'''

from time import sleep
from random import randint
from operator import itemgetter #acessa e ordena os valores em listas, tuplas e dicionários
dado = {}
ranking = ()

for c in range(1, 5):
    dado[f'Jogador {c}'] = randint(1, 6) 

print(f'{"Valores Sorteados":^25}')

for k, v in dado.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

print()
print(f'{"Ranking dos Jogadores":^25}')

ranking = sorted(dado.items(), key = itemgetter(1), reverse = True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
