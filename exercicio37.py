'''Conversor de Bases Numéricas'''

n = int (input('Digite um número inteiro: '))
print ('''Escolha uma das bases para conversão: 
[1] Converter para binário.
[2] Converter para octal.
[3] Converter para hexadecimal.''')
opcao = int (input('Digite sua opção: '))
if opcao == 1:
    print (f'{n} convertido para binário é igual a {bin(n)[2:]}.')
elif opcao == 2:
    print (f'{n} convertido para octal é igual a {oct(n)[2:]}.')
elif opcao == 3:
    print (f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}.')
else:
    print ('Opção inválida, tente novamente.')
# usamos fatiamento para excluir 0b do resultado binario, 0o do resultado
# octal e o 0x do resulado hexadecimal. fizemos isso com o [2:].
