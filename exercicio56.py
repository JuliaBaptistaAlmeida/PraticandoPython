'''Analisador Completo'''

soma = 0
media = 0
nomemaisvelho = ''
idademaisvelho = 0
mulheres = 0
for pessoa in range (1, 5):
    print ('=-' * 5, f'{pessoa}ª PESSOA', '-=' * 5)
    nome = str(input ('Nome: ')).strip()
    idade = int(input ('Idade: '))
    sexo = str(input ('Sexo [M ou F]: '))
    soma += idade
    if pessoa == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    elif sexo in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    elif sexo in 'Ff'and idade < 20:
        mulheres += 1
media = soma / 4
print ('=-' * 20)
print (f'A média da idade dessas pessoas é de {media} anos')
print (f'O homem mais velho tem {idademaisvelho} anos e se chama {nomemaisvelho}.')
print (f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
