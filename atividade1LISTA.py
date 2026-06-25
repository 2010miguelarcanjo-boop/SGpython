alunosSG=["Gabriel Willis Pinheiro Guerra","heitor cavalcante","Miguel Arcanjo","pedro ilberte"]
print ("essa e uma lista de alunos da studio games: "+str(alunosSG))
numero=int(input("digite seu numero da turma: "))
if numero<=-1 :
    print ("seu numero e menor que a lista") 
elif numero>3 :
    print ("seu numero e maior que a lista") 
else :
    print (alunosSG[numero])
