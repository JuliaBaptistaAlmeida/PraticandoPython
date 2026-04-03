'''Funções para votação'''

from datetime import date

def voto(nasc):
    idade = date.today().year - nasc
    print(f'Você tem {idade} anos', end=' ')
    if idade >= 18 and idade <= 60:
        print(f'e o voto é OBRIGATÒRIO.')
    elif idade < 18 and idade >= 16 or idade > 60:
        print(f'e o voto é OPCIONAL.')
    elif idade < 16:
        print(f'e não pode votar.')

#Programa Principal
print(f'VAMOS CONFERIR SE VOCÊ ESTÁ APTO(A) PARA VOTAR')
ano = int(input('Digite seu ano de nascimento: '))
voto(ano)
