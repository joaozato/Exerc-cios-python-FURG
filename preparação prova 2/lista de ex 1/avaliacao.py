def fatorial(num):
    if num ==1:
        return 1
    else:
        return num*fatorial(num-1)


def descobrefatorial(a):
    lista=[]
    cont=0
    cont2=0
    repetida=0
    for i in a:
        lista.append(i)
    while cont < len(lista):
        atual=lista[cont2]
        if lista[cont] == atual:
            repetida+=1
        cont+=1
    return cont

print(descobrefatorial('obaa'))

        
                




