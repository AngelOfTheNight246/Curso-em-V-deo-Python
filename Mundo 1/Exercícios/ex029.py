velocidade = float(input('Qual a velocidade atual do carro ? '))
multa = float(7.00)
if velocidade <= 80:
    print('Seu carro não está excendendo o excesso de velocidado, parabéns!')
else:
    print('Você está acima da velocidade permitida!, Você receberá uma multa de R${:.2f}'.format((velocidade - 80) * 7))