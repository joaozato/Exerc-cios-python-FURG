'''
Questão 4 (1,5 Pontos)

Crie um programa em Python que leia um número inteiro e escreva todos os divisores desse número. Por exemplo:

Número	Divisores
14	    1,2,7,14
17	    1,17
24	    1,2,3,4,6,8,12,24

'''
N= int(input('Digite um número'))
cont=1
lista=[]
while N > 0:
    N2= N/cont
    lista.append(N2)
cont+=1
print(lista)
