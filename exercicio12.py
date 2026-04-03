'''Desconto no Preço'''

preço = float(input ('Qual o valor do produto? R$'))
desconto = (preço * 5) /100
valor = preço - desconto 
print(f'O produto no valor de R${preço:.2f} com 5% de desconto vai custar R${valor:.2f}!')
