'''Funções Aprofundadas'''

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue #volta para o while
        except (KeyboardInterrupt):
            print('ERRO! O usuário não quis digitar um número.')
            return 0
        else:
            return n
        
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real válido.')
        except (KeyboardInterrupt):
            print('ERRO! O usuário não quis digitar um número.')
            return 0
        else:
            return n
        

n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real.')
print()
print(f'O valor inteiro digitado foi {n1} e o número real foi {n2}.')
print()
