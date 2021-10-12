salario = float(input('Qual é o sálario do funcionário ? R$'))
salarioA = float((salario * 10)/ 100)
salarioB = float((salario * 15)/ 100)
if salario > 1250:
    print('O funcionário teve um aumento de 10% no seu sálario, está ganhando mais {:.2f}R$, e seu salário ficou em {:.2f}'.format(salarioA, salario + salarioA))
else:
    print('O funcionário teve um aumento de 15% no seu sálario, está ganhando mais {:.2f}R$, e seu salário ficou em {:.2f}'.format(salarioA, salario + salarioA))