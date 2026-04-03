'''Confederação Nacional de Natação'''

idade = int (input ('Digite a idade do atleta: '))

if idade <= 9:
    print ('Atleta MIRIM.')
elif idade <= 14:
    print ('Atleta INFANTIL')
elif idade <= 19:
    print ('Atleta JUNIOR')
elif idade <= 25:
    print ('Atleta SÊNIOR')
elif idade > 25 and idade <= 90:
    print ('Atleta MASTER')
else:
    print ('Número inválido. Tente novamente.')
    