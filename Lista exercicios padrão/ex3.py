'''

3) Escreva um programa que receba duas listas do usuário e retorne uma nova lista
contendo apenas os elementos comuns entre as duas listas

'''

def similaridades (l1,l2):
    lista=[]
    for i in l1:
        if i in l2:
            lista.append(i)
    return lista


print(similaridades(['bobo', 'patinho','maça','ifood','po'],['tomando','patinho','ifood','banana','gato']))