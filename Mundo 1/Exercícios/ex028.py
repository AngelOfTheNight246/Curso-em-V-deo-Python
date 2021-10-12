from random import randrange
from time import sleep
computador = int(randrange(0, 6)) # Faz o computador "pensar"
print('-' * 20)
jogador = int(input('Tente adivinhar um número de 0 a 5: '))
print('-' * 20)
print('PROCESSANDO...')
sleep(3)
if jogador == computador: 
    print('Seu número foi {}, eu escolhi o número {}, Parabéns, você ganhou o jogo'.format(jogador, computador))
else:
    print('Você escolheu o número {}, enquanto eu escolhi o número {}, Eu venci o jogo'.format(jogador, computador))