'''Alistamento'''

from datetime import date
nasc = int (input ('Informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print (f'Você nasceu em {nasc} e possui {idade} anos em {ano}.')
if idade < 18:
    saldo = 18 - idade
    alistar = ano + saldo
    print (f'Você ainda não pode se alistar. Faltam {saldo} para você completar a maioridade.')
elif idade > 18:
    saldo = idade - 18
    alistar = ano - saldo
    print (f'Você deveria ter se alistado há {saldo} anos. Você precisa se alistar IMEDIATAMENTE.')
else: 
    print (f'Você possui {idade} anos e já pode se alistar.')
