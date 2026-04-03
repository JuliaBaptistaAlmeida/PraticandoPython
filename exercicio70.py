'''Estatísticas em Produtos'''

print('=-' * 13)
print('LOJA DO SEU TOBA')
print('=-' * 13)

c = menor = total = maismil = 0
barato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor: R$ '))
    c += 1
    total += valor
    if valor >= 1000:
        maismil +=1
    if c == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto

    resposta = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Dados inválidos. Digite S para sim e N para não: ')).upper().strip()[0]
    if resposta == 'N':
        break

print(f'O total da compra foi de R$ {total:.2f}.')
print(f'Temos {maismil} produtos com mais de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} e custou R$ {menor:.2f}.')
