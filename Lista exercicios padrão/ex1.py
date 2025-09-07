'''

1) Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista
contendo apenas as palavras com mais de 5 caracteres.

'''

def cinco_mais (palavras):
    lista=[]
    for i in palavras:
        if len(i) >= 5:
            lista.append(i)
    return lista


print(cinco_mais(['maça','banana','kalinga','ifood','pera','ovo','matutando']))
