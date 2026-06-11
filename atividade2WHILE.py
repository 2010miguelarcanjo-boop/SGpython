import random
pergunta=0
nmax=int(input('digite o numero maximo: '))
nsecret=random.randint(1,nmax)
chances=int(input('digite suas chances: '))
while pergunta != nsecret and chances>0:
    pergunta=int(input('digite seu numero aqui: '))
    if pergunta>nsecret:
        print ('seu numero e maior que o certo')
        chances-=1
    elif pergunta<nsecret:
        print ('seu numero e menor que o certo')
        chances-=1
    else:
        print ('voce acertou')
    if chances<=0:
        print('voce perdeu')
        print (f'o numero certo era {nsecret}')
