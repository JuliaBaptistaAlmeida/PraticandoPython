'''Verificando se o nome da cidade COMEÇA com Santo'''

cidade = str(input ('Qual o nome da cidade em que você nasceu? ')).strip()
print (f'Sua cidade começa com Santo?' , {cidade[:5].upper() == 'SANTO'})