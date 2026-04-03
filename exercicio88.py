'''Palpites Para a Mega Sena'''

from random import randint

jogos = []

print('=-' * 15)
print(f'{'MEGA SENA':^30}')
print('=-' * 15)

quant = int(input('Quantos palpites você deseja ver? '))
total = 1

while total <= quant:
    lista = []
    while len(lista) < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)

    lista.sort()
    jogos.append(lista)
    total += 1

print('Os jogos sorteados foram:')
for num, jogo in enumerate(jogos, 1): #para começar em jogo 1 e nao 0
    print(f'Jogo {num}: {jogo}')
print('=-' * 15)
