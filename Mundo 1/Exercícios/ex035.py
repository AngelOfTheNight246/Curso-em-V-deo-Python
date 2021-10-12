n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('As retas podem sim formar um Triângulo!!!')
else:  
    print('Elas não podem formar um triângulo!!!')