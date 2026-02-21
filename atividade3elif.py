idade=int(input('digite sua idade: '))
ingresso= input('tem ingresso? ')
autorizacao= input('tem autorizacao? ')
VIP= input('tem VIP? ')
if idade<12 :
    print ('voce nao pode entrar!')
elif idade >=18 and ingresso=='sim' :
    print ('pode passar')
elif idade<18 and autorizacao=='sim' and ingresso=='sim' :
    print ('pode entrar mas to de olho!')
elif VIP=='sim' :
    print ('voce e convidado especial!')
else :
    print ('negado!')
