'''

4) Dada uma lista de números inteiros informada pelo usuário, escreva um programa
em Python que conte quantos números únicos (diferentes) estão presentes na lista.
A digitação dos elementos da lista deve encerrar quando for digitado o número zero.

'''
def numero_unico(n):
    lista=[n]
    while n != 0:
        n = int(input('Digite um número'))
        lista.append(n)
    unicos=set(lista)
    tamanho=len(unicos)-1
    return tamanho
    

a=int(input('Digite um número'))
print(numero_unico(a))
