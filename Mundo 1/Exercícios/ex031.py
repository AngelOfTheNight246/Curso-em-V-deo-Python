distância = float(input('Qual a distância da viagem ? '))
if distância <= 200:
    print('Você fará uma viagem de 200 ou menos KM, então sua passagem ficara por R${:.2f}'.format(distância * 0.50))
else:
    print('Você fará uma viagem de mais de 200Km, então sua passagem ficara R${:.2f}'.format(distância * 0.45))