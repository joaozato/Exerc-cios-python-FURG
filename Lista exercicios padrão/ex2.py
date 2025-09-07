'''

2) Escreva um programa que receba uma lista de números e retorne uma nova lista
contendo apenas os números pares.

'''

def numeros_pares (n):
    lista=[]
    for i in n:
        if i%2 ==0:
            lista.append(i)
    return lista


print(numeros_pares([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))