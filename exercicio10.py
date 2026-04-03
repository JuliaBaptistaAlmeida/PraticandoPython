'''Conversor de Moedas'''

real = float(input ('Quanto (em R$) você tem na carteira? '))
dolar = real / 5.43
print(f'Com R$ {real:.2f}, você pode comprar US$ {dolar:.2f}.')
