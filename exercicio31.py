'''Preço de Uma Viagem'''

distancia = int(input ('Qual será a distância de sua viagem? '))
if distancia <= 200:
    valor1 = distancia * 0.50
    print (f'Você pagará R$ {valor1:.2f} em sua viagem de {distancia}km.')
else:
    valor2 = distancia * 0.45
    print (f'Você pagará R$ {valor2:.2f} em sua viagem de {distancia}km.')
