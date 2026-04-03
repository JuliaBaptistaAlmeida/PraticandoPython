'''Catetos e Hipotenusa'''
# Com importação do módulo math

from math import hypot
co = float(input ('Digite o comprimento do cateto oposto: '))
ca = float(input ('Digite o comprimento do cateto adjacente: '))
hi = hypot (co, ca)
print (f'A hipotenusa do triângulo retângulo mede {hi:.2f}')
