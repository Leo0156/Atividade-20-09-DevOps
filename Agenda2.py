print("\\Bem vindo a Agenda Beta") 

nome=[]
rua=[]
cep=[]
bairro=[]
estado=[]
telefone=[]
cont = 's'
x=0
linha = "_________________________________________________________________"

while cont == 's' or cont == 's' : 
    nome.append (input ("Seu nome: "))
    nome1 = nome[x]

    rua.append (input ("Sua Rua: "))
    rua1 = rua [x]

    cep.append (input ("Seu Cep: "))
    cep1 = cep [x]

    bairro.append (input ("Seu Bairro: "))
    bairro1 = bairro [x]

    
    estado.append (input ("Seu estado: "))
    estado1 = estado [x]
    
    telefone.append (input ("Seu Telefone: "))
    telefone1 = telefone [x]

    cont=input("pressione (s) para adicionar mais 1 arquivo Ou \nPressione (n) para parar\n")
    x+=1
    print (linha)
    print ()

    with open ("Agenda.txt", "a") as arq: # PARA ABRIR O ARQUIVO 
        arq.write ("Seu nome é "+nome1+"\n")
        arq.write ("Seu rua é "+rua1+"\n")
        arq.write ("Seu cep é "+cep1+"\n")
        arq.write ("Seu bairro é "+bairro1+"\n")
        arq.write ("Seu estado é "+estado1+"\n")
        arq.write ("Seu telefone é "+telefone1+"\n")
        arq.write (""+linha+"\n")
    arq.close()

pes= (input("Digite o Nome para a pesquisa :"))
for x in range (len(nome)):
    if pes == nome[x]:
        print ("Seu Nome é", nome[x])
        print ("Seu rua é", rua[x])
        print ("Seu cep é", cep[x])
        print ("Seu bairro é", bairro[x])
        print ("Seu estado é", estado[x])
        print ("Seu telefone é",telefone[x])
    else:
        print("Nome não encontrado")


