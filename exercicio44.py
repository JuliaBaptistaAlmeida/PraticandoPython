'''Caixa de Autoatendimento'''
#Utilizei while

print (f'{" LOJA DO SEU TOBA ":=^40}')
preco = float(input ('Valor total das compras: R$'))
print ('''FORMAS DE PAGAMENTO
[1] Pix
[2] à vista no cartão
[3] 2X no cartão
[4] 4X até 6X no cartão''')
pagamento = int(input ('Selecione a opção desejada: '))
while pagamento not in [1, 2, 3, 4]:
    print('Número inválido. Tente novamente.')
    pagamento = int(input('Selecione a opção desejada: '))

if pagamento == 1:
    total = preco - (preco * 10 / 100)
    print('No pagamento à vista você terá um desconto de 10%.')
    print(f'Sua compra de R${preco:.2f} sairá por R${total:.2f}.')
elif pagamento == 2:
    total = preco - (preco * 5 / 100)
    print('Nessa forma de pagamento você terá um desconto de 5%.')
    print(f'Sua compra de R${preco:.2f} sairá por R${total:.2f}.')
elif pagamento == 3:
    total = preco / 2
    print(f'O valor total é de R${preco:.2f}. Duas parcelas de R${total:.2f}.')
    print('Aproxime ou insira o cartão.')
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    xcartao = 0
    while xcartao not in [4, 5, 6]:
        xcartao = int(input('Selecione o número de parcelas (4 a 6): '))
        if xcartao not in [4, 5, 6]:
            print('Número inválido. Tente novamente.')
    parcela = total / xcartao
    print('Nessa forma de pagamento há um juros de 20%.')
    print(f'O valor total é de R${total:.2f}. {xcartao} parcelas de R${parcela:.2f}.')
    print('Aproxime ou insira o cartão.')
    