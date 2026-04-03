'''Tabuada parte 3'''

c = 1
print ('''Vamos ver a tabuada de um valor?!
Para interromper digite um valor negativo!''')
print ('=-' * 15)
while True:
        n = int (input('Digite o número da tabuada desejada: '))
        print ('=-' * 15)
        if n < 0:
                break
        for c in range (1, 11):
                print (f'{n} X {c} = {n * c}')
                c += 1
print ('PROGRAMA ENCERRADO! FIM!')
