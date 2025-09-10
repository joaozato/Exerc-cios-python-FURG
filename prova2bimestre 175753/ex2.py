'''

2) (2,5 Pontos) Crie uma função que seja um particionador de listas. Ela deve receber
como parâmetro uma lista e um número N. Você deve retornar uma lista de listas
com o tamanho dado. Veja o exemplo:

'''


#feito também, funcional graças a Deus

def particiona (lista,n):
    listagrande=[]
    listasub=[]
    cont=0
    cont2=0
    cont3=0
    for i in lista:
        cont+=1
        listasub.append(i)
        if len(listasub) ==3:
            cont=0
            listagrande.append(listasub)
            listasub=[]
    return listagrande







listona=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']

print(particiona(listona,3))
