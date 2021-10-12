nome = str(input('Digite seu nome: '))
nomemai = nome.upper()
nomemin = nome.lower()
total = len(nome.replace(" ", ""))
prinome = nome.split()
qprinome = len(prinome[0])
print(' Nome: {0} \n Nome com letras maiúsculas: {1} \n Nome com letras minúsculas: {2} \n Letras ao todo: {3} \n Letras primeiro nome: {4}'.format(nome, nomemai, nomemin, total, qprinome))

#PUTA QUE PARIU MEU CÓDIGO TA COMPLETAMENTE CAGADO DIGNO DE UMA ENGENHOCA

#Versão Guanabara 

#nome = str(input('Digite seu nome completo: ')).strip
#print('Analisando seu nome')
#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas  é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
