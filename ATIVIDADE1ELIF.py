nota1=float(input('digite sua nota: ' ))
nota2=float(input('digite sua nota: ' ))
nota3=float(input('digite sua nota: ' ))
media=(nota1+nota2+nota3)/3
if media<5:
    print ('reprovado F')
elif media<6:
    print ('aprovado F')
elif media<7:
    print ('aprovado D')
elif media<8:
    print ('aprovado C')
elif media<9:
    print ('aprovado B')
elif media<10:
    print('aprovado A')
else :
    print ('nota perfeita A')
