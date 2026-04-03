'''Progressão Aritmética/ PA parte 2''' 
#a parte 1 é o exercicio 51
#sem usar fórmula matematica

primeirotermo = int(input ('Digite o Primeiro Termo: ')) #onde começa
razao = int(input ('Digite a Razão: ')) #quantos pula
termo = primeirotermo
c = 1
while c <= 10:
    print (f'{termo} ->', end= ' ')
    termo += razao
    c += 1
print ('FIM!')
