'''Aluguel de Carros'''

km = float(input ('Quantos km foram percorridos? '))
dias = int(input ('Por quantos dias o carro foi alugado? '))
valor = (km * 0.15) + (dias * 60)
print (f'O valor total a pagar é de R${valor:.2f}.')
