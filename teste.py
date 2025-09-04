texto='ABCDDDEEFGHIJKKKKOP'

maior_letra=texto[0]
maior_contagem=1
letra_atual=texto[0]
contagem_atual=1

for i in range(1,len(texto)):
    if texto[i] == letra_atual:
        contagem_atual+=1
    else:
        letra_atual=texto[i]
        contagem_atual=1

    if contagem_atual>maior_contagem:
        maior_contagem=contagem_atual
        maior_letra=letra_atual
print( 'a maior letra é', maior_letra, 'e foi repetida ',maior_contagem,'vezes')
