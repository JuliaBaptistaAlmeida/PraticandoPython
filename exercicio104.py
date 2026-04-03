'''Validando Entrada de Dados'''

def leiaint(msg):
    
    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
            print()
        if ok:
            break
    return valor

#Programa Principal
n = leiaint('Digite um número: ')
print()
print(f'Você digitou o número {n}')
print()
