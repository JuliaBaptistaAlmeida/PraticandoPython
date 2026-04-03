'''Separando Algarismos'''

import random 
num = random.randint(0, 9999)
n = str(num)
print (f'O número sorteado é {num}.')
print (f'A unidade é {n[3]}.')
print (f'A dezena é {n[2]}.')
print (f'A centena é {n[1]}.')
print (f'A unidade de milhar é {n[0]}.')
