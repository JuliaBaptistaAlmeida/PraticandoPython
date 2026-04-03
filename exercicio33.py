'''Maior e Menor'''

print ('Vamos analisar qual o maior e o menor número...')
n1 = int(input ('Digite o valor 1: '))
n2 = int(input ('Digite o valor 2: '))
n3 = int(input ('Digite o valor 3: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2: 
    maior = n3
print ('-=-' * 8)
print (f'O maior número é {maior}.')
print (f'O menor número é {menor}.')
