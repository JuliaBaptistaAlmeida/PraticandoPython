'''Jogo de Adivinhação'''

import random
from time import sleep
computador = random.randint (0, 5)
print ('-=-' * 15)
print ('Eu pensei em um número de 0 a 5. Tente adivinhar...')
print ('-=-' * 15)
jogador = int(input ('Qual seu palpite? '))
print ('PROCESSANDO...')
sleep (3)
if jogador == computador:
    print ('Parabéns, você GANHOU!')
else:
    print (f'Poxa, você PERDEU, eu pensei em {computador}.')
