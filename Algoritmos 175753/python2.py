
#crie a função que crie siglas apenas com letras



#crie a função agora com numeração estilo C3


'''
def sigla (n):
    lista=''
    nao_pode=['da','do','de','Para','para','DE','DO','DA']
    divisor=n.split(' ')
    for i in divisor:
        if i not in nao_pode:
            lista+=i[0] 
    return compacta (lista)


print(sigla('mundo furg'))
'''

def compacta(n):
    saida= n[0]
    cont=1
    i= 1
    while i <len(n):
        letra = n [i]
        if letra == saida[-1]: #se é igual ao ultimo
            cont +=1
        else:
            if cont>1:
                saida += str(cont)
                cont=1
            saida += n[i]
        i +=1
    if cont >1: #caso  tenha ficado um resto quando termina em repetição
        return saida

def sigla (n):
    lista=''
    nao_pode=['da','do','de','Para','para','DE','DO','DA']
    divisor=n.split(' ')
    for i in divisor:
        if i not in nao_pode:
            lista+=i[0] 
    return compacta (lista)


print(sigla('centro de ciencias computacionais'))


