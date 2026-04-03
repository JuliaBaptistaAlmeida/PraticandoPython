'''Radar de Velocidade'''

velocidade = int(input ('Qual a velocidade atingida pelo carro? '))
multa = float(velocidade - 80) * 7
if velocidade <= 80:
    print ('Você está dentro do limite de velocidade, tenha um bom dia!')
else:
    print (f'Você ultrapassou o limite de velocidade de 80km/h e será multado(a) em R$ {multa:.2f}. Dirija com cuidado!')
