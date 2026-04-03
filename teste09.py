'''Aprendendo Módulos: math'''

from math import sqrt, ceil, floor
n = int(input ('Digite um número: '))
raiz = sqrt (n)
print (f'A raiz quadrada de {n} é igual a {raiz}.')
print (f'A raiz quadrada de {n} é {ceil (raiz):.2f} se arredondarmos para cima.')
print (f'A raiz quadrada de {n} é {floor (raiz):.2f} se arredondarmos para baixo.')
