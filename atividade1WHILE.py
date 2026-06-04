pergunta=0
nsecret=10
while pergunta != nsecret:
    pergunta=int(input('digite seu numero aqui: '))
    if pergunta>nsecret:
        print ('seu numero e maior que o certo')
    elif pergunta<nsecret:
        print ('seu numero e menor que o certo')
    else:
        print ('voce acertou')

