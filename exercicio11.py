'''Pintando Parede'''

altura = float(input ('Qual a altura da parede? '))
largura = float(input ('Qual a largura da parede? '))
area = altura * largura
tinta = area / 2
print(f'A aréa desta parede é de {area:.2f}m², sendo necessário {tinta:.2f}L de tinta para pintá-la.')
