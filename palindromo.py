'''
Escreva um programa em python que diga se uma palavra é palindromo.
exemplo
Ana
é palindromo

'''

def palindromo (p):
    reverso=''
    cont=0
    for i in p[::-1]:
        reverso= reverso+i
    while cont < len(p):
        if p[cont] == reverso[cont]:
            cont+=1
        else:
            return 'não é palindromo'
    return 'é palindromo'
    
    
    


a=input('Digita uma palavra')
print(palindromo(a))