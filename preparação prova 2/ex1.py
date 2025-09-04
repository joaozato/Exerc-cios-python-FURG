'''
Claro! Aqui estão alguns exercícios de funções em Python que focam especificamente na manipulação de strings e listas, com diferentes níveis de complexidade.

Nível Iniciante
Exercício 1: Filtrar Palavras por Comprimento
Objetivo: Criar uma função que receba uma frase e retorne uma lista contendo apenas as palavras com um comprimento maior que um determinado número.

Descrição:
Escreva uma função chamada filtrar_palavras que aceite dois argumentos: uma string frase e um número inteiro comprimento_minimo. A função deve dividir a frase em palavras e retornar uma nova lista contendo apenas as palavras cujo comprimento é maior ou igual a comprimento_minimo.

'''

def filter (words,size):
    listofwords=[]
    cuting = words.split()
    for i in cuting:
        if len(i) >= size:
            listofwords.append(i)
    return listofwords
        
        
    
print(filter("pedro paulo sabia que dividindo posteriormente devendose", 7))