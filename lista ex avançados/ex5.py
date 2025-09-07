'''
5. Ordenação de Palavras por Critério Personalizado
Escreva uma função `ordenar_palavras(frase)` que:
1. Separe a frase em palavras,
2. Ordene as palavras primeiro pelo tamanho e depois em ordem alfabética.
Exemplo:
Entrada: "banana uva abacaxi pera morango"
Saída: ["uva", "pera", "banana", "abacaxi", "morango"]

'''

def ordenar_palavras (frase):       
    separar=frase.split()    #aqui separa por espaços, coloca tudo numa lista
    tamanhos=sorted(separar, key=len)  #aqui ele separa por tamanho, logo por ordem alfabetica também
    return tamanhos
        


print(ordenar_palavras("banana uva abacaxi pera morango"))