'''Grupo de maioridade'''

from datetime import date
hoje = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range (1, 8):
    ano = int (input (f'Em que ano nasceu a {pessoa}ª pessoa? '))
    idade = hoje - ano
    if idade >= 18:
        totalmaior += 1 #o mesmo que colocar totalmaior = totalmaior + 1
    else:
        totalmenor += 1
print (f'Ao todo tivemos {totalmaior} pessoas maiores de idade e {totalmenor} menores de idade.')