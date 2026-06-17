import random
pergunta=0
nmax=int(input('digite o numero maximo: '))
nsecret=random.randint(1,nmax)
chances=int(input('digite suas chances: '))
while pergunta != nsecret and chances>0:
    pergunta=int(input('digite seu numero aqui: '))
    if pergunta>nsecret:
        print ('escolha um numero menor')
        chances-=1
    elif pergunta<nsecret:
        print ('escolha um numero maior')
        chances-=1
    else:
        print ('voce acertou')
    if chances<=0:
        print('voce perdeu')
        print (f'o numero certo era {nsecret}')
