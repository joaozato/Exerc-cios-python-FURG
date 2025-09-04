'''
1) Faça um programa em python que leia uma frase e a passe para maiúscula. Você não
deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.

'''

def maiuscula(frase):
    lista=[]
    grande=''
    cont= 0
    while cont <len(frase):
        if frase[cont] == ' ':
            lista.append(frase[cont])
            grande=grande +frase[cont]
        else:
            lista.append(frase[cont])
            a =chr(ord(lista[cont]) -32)
            grande=grande+a
        cont+=1     
    return grande

print(maiuscula('porra que merda inferno que cu essa bosta que saco'))

#['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']