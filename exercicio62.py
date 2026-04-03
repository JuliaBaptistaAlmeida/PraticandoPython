'''Progressão Aritmética/ PA parte 3'''
#os outros são 61 e 51

primeirotermo = int(input ('Digite o Primeiro Termo: ')) #onde começa
razao = int(input ('Digite a Razão: ')) #quantos pula
termo = primeirotermo
c = 1
total = 0
mais = 10 #pra mostrar inicialmente 10 termos
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? (0 para sair) '))

print(f'Progressão finalizada com {total} termos mostrados.')