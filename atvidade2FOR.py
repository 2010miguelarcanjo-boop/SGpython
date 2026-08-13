palavra=input("me diga uma palavra: ")
m=False
i=False
g=False
u=False
e=False
l=False
for letra in palavra:
    if letra=="m" or letra=="M":
        print(letra+" esta no meu nome")
        m=True 
    elif letra=="i" or letra=="I":
        print(letra+" esta no meu nome")
        i=True 
    elif letra=="g" or letra=="G":
        print(letra+" esta no meu nome")
        g=True 
    elif letra=="u"or letra=="U":
        print(letra+" esta no meu nome")
        u=True 
    elif letra=="e"or letra=="E":
        print(letra+" esta no meu nome")
        e=True 
    elif letra=="l"or letra=="L":
        print(letra+" esta no meu nome")
        l=True     
    else:
        print(letra+" não está no meu nome")
print ("meu nome é: ")
if m==True:
    print("M")
else:
    print ("-")
if i==True:
    print("i")
else:
    print ("-")
if g==True:
    print("g")
else:
    print ("-")
if u==True:
    print("u")
else:
    print ("-")
if e==True:
    print("e")
else:
    print ("-")
if l==True:
    print("l")
else:
    print ("-")
