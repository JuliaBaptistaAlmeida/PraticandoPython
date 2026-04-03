'''Jogo de Adivinhação'''

import random 
numero = random.randint (0, 5)
print ('Olá, bem vindo(a) ao jogo "Adivinhe". Eu pensei em um número de 0 a 5 e você tem que tentar adivinhá-lo')
palpite = int(input ('Qual é seu palpite de adivinhação? '))
if palpite == numero:
    print (f'Parabéns, você venceu! 🎉')
else:
    print (f'Poxa, você perdeu, eu pensei em {numero}!')
print ('Espero que tenha se divertido, que tal jogar novamente? 💚')
