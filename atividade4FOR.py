perguntas=["em que cromossomo ocorre a trissomia da sinrome de down? ", 
          "quem foi o general do grupo revolucionario responsavel por liderar as guerras napoleonicas? ", 
          "pedro alvares cabral descobriu o brasil pensando ser as indias?"]
respostasCertas=["21","napoleao","nao"]
indice=0
acertos=0
for pergunta in perguntas:
    print(pergunta)
    respostas=input('digite sua resposta: ')
    if respostas==respostasCertas[indice]:
        acertos+=1
        print ('você acertou: '+ str(acertos))
    else:
        print("voce errou!")
    indice+=1
if acertos==3:
    print ('parabens!acertou todos!!!')
elif acertos==2:
    print ('parabens voce passou!')
else:
    print('nao foi desta vez...')
