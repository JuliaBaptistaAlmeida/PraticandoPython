'''Políndromo'''
#usando o for

frase = str(input ('Digite uma frase: ')) .strip().upper()
palavras = frase.split()
junto = '' . join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print (f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print ('A frase é um PALÍNDROMO!')
else:
    print ('A frase é NÃO é um palíndromo!')
