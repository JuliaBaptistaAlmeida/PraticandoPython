'''Progressão Aritmética/ PA'''
#usando solução matemática

primeirotermo = int(input ('Digite o Primeiro Termo: ')) #onde começa
razao = int(input ('Digite a Razão: ')) #quantos pula
decimotermo = primeirotermo + (10 - 1) * razao #fórmula para achar o decimo termo e não o caractere 10
for pa in range(primeirotermo, decimotermo + razao, razao):
    print (f'{pa}', end = ' ')
