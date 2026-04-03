'''Verificando se o nome tem Silva em QUALQUER lugar'''

nome = str(input ('Qual seu nome completo? ')).strip()
print (f'Seu nome tem Siva?', {'SILVA' in nome.upper()})
