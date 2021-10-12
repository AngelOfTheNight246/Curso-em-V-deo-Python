km = float(input('Quantos kilômetros você percorreu com esse carro ?'))
d = float(input('Por quantos dias você alugou esse carro ?'))
cd = float(d * 60)
kmd = km * 0.15
pf = kmd + cd
print('O preço final fica por {}R$'.format(pf))