'''Seno, Cosseno e Tangente'''

from math import sin, cos, tan, radians
angulo = float(input ('Digite o valor de um ângulo: '))
s = sin (radians (angulo))
c = cos (radians (angulo))
t = tan (radians (angulo))
print (f'O ângulo de {angulo} tem o SENO de {s:.2f}')
print (f'O ângulo de {angulo} tem o COSSENO de {c:.2f}')
print (f'O ângulo de {angulo} tem a TANGENTE de {t:.2f}')
