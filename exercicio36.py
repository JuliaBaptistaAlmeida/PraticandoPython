'''Empréstimo para compra de casa'''

casa = float(input ('Qual o valor total da casa? R$ '))
salario = float(input ('Qual seu salário atual? R$ '))
anos = int(input ('Em quantos anos você deseja pagar? '))
valor = (salario * 30) / 100
prestacao = casa / (anos * 12)
print (f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos', end='')
print (f' a prestação será de R$ {prestacao:.2f}')
if prestacao <= valor:
    print ('Empréstimo APROVADO!')
else:
    print ('Empréstimo NEGADO!')
