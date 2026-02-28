idade= int(input('insira sua idade '))
experiencia=(input('tem experiencia? '))
anteecedentes= (input('tem antecedentes? '))
ensinospr= (input('tem ensino superior ? '))
indi= (input('alguem te indicou? '))
if experiencia== 'sim' and idade>=18 and anteecedentes=='nao':
    print ('vamos para uma entrevista!')
elif experiencia== 'nao' and (ensinospr=='sim' or indi=='sim' )and anteecedentes=='nao':
    print ('vamos para uma entrevista!')
else :
    print ('vamos te deixar na lista de espera')
