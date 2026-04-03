'''Pedra, Papel, Tesoura'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua escolha? '))
if jogador < 0 or jogador > 2:
    print ('Opção inválida!')
    exit ()
print ('JO')
sleep (1)
print ('KEN')
sleep (1)
print ('PÔ!!!')
sleep (1)
print('-=' * 20)
print(f'Computador escolheu {itens[pc]}')
print(f'Jogador escolheu {itens[jogador]}')
print('-=' * 20)
if pc == jogador:
    print('EMPATE!')
elif (pc == 0 and jogador == 1) or (pc == 1 and jogador == 2) or (pc == 2 and jogador == 0):
    print('Jogador VENCEU!')
else:
    print('Computador VENCEU!')
