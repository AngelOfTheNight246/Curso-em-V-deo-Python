fun = input('Qual é o nome do funcionário ?')
s1 = float(input('Qual era o antigo salário dele ?'))
s2 = float((s1 * 15) / 100)
sfinal = float((s1 + s2))
print('O funcionário {} ganhava um salário de {} reais, com o aumento de 15% passou a ganhar {:.2f}'.format(fun, s1, sfinal))