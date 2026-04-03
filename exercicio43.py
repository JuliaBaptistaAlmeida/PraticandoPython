'''Ìndice de Massa Corporal'''

peso = float(input ('Qual é o seu peso? '))
altura = float(input ('Qual a sua altura? '))
imc = peso / (altura * altura)
print (f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print ('Você está abaixo do peso!')
elif imc > 18.5 and imc <= 24.99:
    print ('Peso ideal: Continue assim!')
elif imc >= 25 and imc <= 29.99:
    print ('Sobrepeso: Você está acima do peso!')
elif imc > 30 and imc <= 39.99:
    print ('Obesidade: Você está muito acima do peso!')
elif imc > 40:
    print ('Obesidade mórbida: Procure um médico e nutricionista!')
else:
    print ('Número inválido. Tente novamente!')
    