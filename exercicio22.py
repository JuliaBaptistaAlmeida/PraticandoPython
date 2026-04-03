'''Analisando um Nome'''

nome = str(input ('Qual o seu nome completo? ')).strip()
print (f'Seu nome com letras maiúsculas fica: {nome.upper()}')
print (f'Seu nome com letras minúsculas fica: {nome.lower()}')
nome2 = nome.replace(' ', '')
print (f'Seu nome tem {len(nome2)} letras.')
print (f'Seu primeiro nome tem {nome.find(' ')} letras.') #vai contar até o primeiro espaço
