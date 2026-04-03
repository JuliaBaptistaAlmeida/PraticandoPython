'''Funções para Sortear e Somar'''

from random import randint

def sorteio(n):
    print('~~' * 25)
    print(f'Os 5 números sorteados foram: {n}')
    print('~~' * 25)
def somapar(num):
    print(f'A soma dos números pares é igual a {num}')
    print('~~' * 25)
    print()

lista = []
par = []
soma = 0

for c in range(5):
    numeros = randint(1, 10)
    lista.append(numeros)
    if numeros % 2 == 0:
        par.append(numeros)
        soma += numeros

sorteio(lista)
somapar(soma)
