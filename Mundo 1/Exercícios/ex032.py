from datetime import date
from time import sleep
ano = int(input('Digite o ano para analisar ? coloque 0 para analisar o ano atual: '))
print('ANALISANDO...')
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um ano Bissexto! :)')
else:
    print('Não é um ano Bissexto :(')