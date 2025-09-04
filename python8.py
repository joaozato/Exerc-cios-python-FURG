def contarvogais (texto):
    texto.upper
    vogais=['A','E','I','O','U','a','e','i','o','u']
    cont=0
    for i in texto:
        if i in vogais:
            cont+=1
    return 'a sentença contem ',cont ,'vogais'

print(contarvogais('abacaxi'))