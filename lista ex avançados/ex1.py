'''
1. Palíndromos Recursivos
Implemente uma função recursiva `eh_palindromo(texto)` que receba uma string e retorne
`True` se for palíndromo (desconsiderando espaços, acentos e diferenças entre
maiúsculas/minúsculas) e `False` caso contrário.
Exemplo:
Entrada: "Socorram-me subi no onibus em Marrocos"
Saída: True



'''

def palindromo (p):
    reverso=''
    cont=0
    for i in p[::-1]:
        reverso= reverso + i
    while cont <len(p):
        if p[cont] == reverso[cont]:
            cont+=1
        else:
            return False
    return True

print (palindromo('oba'))