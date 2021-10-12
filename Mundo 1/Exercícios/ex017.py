from math import hypot
catetoO = float(input('Digite o comprimento do Cateto Oposto: '))
catetoA = float(input('Digite o comprimento do Cateto Adjacente: '))
hipotenusa = hypot(catetoO, catetoA)
print('A hipotenusa é {:.2f}'.format(hipotenusa))

