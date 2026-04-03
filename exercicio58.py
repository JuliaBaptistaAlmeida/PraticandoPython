'''Jogo de Advinhação parte 2''' 
#a parte 1 é o exercicio 28

from random import randint
from time import sleep
numero = randint (0, 10)
print ('Olá, eu sou seu computador!')
print ('''Vamos brincar de adivinhe? 
       Eu pensei em um número de 0 a 10, você consegue acertar?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int (input ('Qual é o seu palpite? '))
    palpite += 1
    if jogador == numero:
        acertou = True
        print ('Eu escolhi...')
        sleep (2)
        print (f'{numero}!!!')
        print ('Parabéns, você venceu! 🎉')
    else:
        if jogador < numero:
            print ('Mais... Tente mais uma vez!')
        elif jogador > numero:
            print ('Menos.. Tente mais uma vez.')
print (f'Acertou com {palpite} tentativas!', end = ' ')
print ('Espero que tenha se divertido, que tal jogar novamente? 💚')