'''

5) Faça um programa em python em que o usuário digite uma lista de números inteiros
(até digitar zero). Após, o programa deve mostrar a frequência de cada número na
lista, ou seja, quantos números 1 tem, quantos números 2, etc

'''

def numero_unico(n):
    cont=0
    lista=[n]
    ocorrencias=[]
    repetidos=[]
    while n != 0:
        n = int(input('Digite um número'))
        lista.append(n)
    for i in lista:
        contaprimeiro=lista.count(i)
        ocorrencias.append(contaprimeiro)
        
            
        
        
    return lista, ocorrencias

    
    
    

a=int(input('Digite um número'))
print(numero_unico(a))