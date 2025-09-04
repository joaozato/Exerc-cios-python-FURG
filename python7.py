#encontrar o maior numero em uma lista

def maior (conjunto):
    maior_de_todos = conjunto[0]
    for i in conjunto:
        if i > maior_de_todos:
            maior_de_todos = i
    return maior_de_todos
    
            

            
numeros=[2,4,8,15,3,20,5]
print(maior(numeros))