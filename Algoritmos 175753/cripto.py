
def compacta(final,chave):
    end=''
    for i in final:
        end += chr(ord(i) - chave)
    return end



def criptografia (nome, chave):
    final=''
    for i in nome:
        final += chr(ord(i) + chave)
    return compacta(final,chave)


print(criptografia('Kirekulim',4))


    






