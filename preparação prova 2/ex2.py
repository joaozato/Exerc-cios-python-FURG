'''

Exercício 2: Iniciais dos Nomes
Objetivo: Criar uma função que receba uma lista de nomes completos e retorne uma lista com as iniciais de cada nome.

Descrição:
Escreva uma função chamada extrair_iniciais que receba uma lista de strings, onde cada string é um nome completo. A função deve retornar uma nova lista contendo as iniciais de cada nome. Por exemplo, para "Ada Lovelace", a inicial seria "AL".




'''

def initials (fullnames):
    initialsnames=[]
    strings=''
    cont=0
    strings2=''
    end=[]
    for i in fullnames:
        strings += i
        a = strings.upper()
    for i in strings:
        if i == a[cont]:
            initialsnames.append(i)
        cont+=1
    for i in initialsnames:
        if i != ' ':
            strings2 += i
        cont =0
    while cont < len(strings2):
        




print(initials(["Ada Lovelace", "Grace Hopper", "Alan Turing"]))