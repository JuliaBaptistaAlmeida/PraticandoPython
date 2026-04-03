'''Primeira e última ocorrência de um nome'''

frase = str(input ('Coloque sua frase aqui: ')).upper().strip()
print (f'Quantas vezes aparece a letra A na frase? ', {frase.count('A')})
print (f'Qual a posição do primeiro A? ', {frase.find ('A') +1}) # para começar a contar de 1 e não 0
print (f'Qual a posição do último A? ', {frase.rfind ('A') +1})
