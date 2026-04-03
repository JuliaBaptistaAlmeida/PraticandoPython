'''Sorteando um aluno'''
# Com importação do módulo random

from random import choice
a1 = str(input('Primeiro(a) aluno(a): '))
a2 = str(input ('Segundo(a) aluno(a): '))
a3 = str(input ('Terceiro(a) aluno(a): '))
a4 = str(input ('Quarto(a) aluno(a): '))
lista = [a1, a2, a3, a4]
resultado = choice (lista)
print (f'O(a) aluno(a) sorteado(a) foi: {resultado}.')
