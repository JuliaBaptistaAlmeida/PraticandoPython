'''Políndromo'''
#sem usar o for

frase = str(input ('Digite uma frase: ')) .strip().upper()
palavras = frase.split()
junto = '' . join(palavras)
inverso = junto[::-1]
print (f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print ('A frase é um PALÍNDROMO!')
else:
    print ('A frase é NÃO é um palíndromo!')
