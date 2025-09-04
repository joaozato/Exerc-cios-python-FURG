def maiorletra_enumero (texto):
    maior_letra= texto[0]
    letra_atual= texto[0]
    maior_contagem=1
    contagem_atual=1
    for i in range(1, len(texto)):
        if texto[i] == letra_atual:
            contagem_atual+=1
        else:
            letra_atual=texto[i]
            contagem_atual=1
        if contagem_atual>maior_contagem:
            maior_contagem=contagem_atual
            maior_letra=letra_atual
    return 'a letra mais repetida é ',maior_letra, 'com incidencia de ',maior_contagem

print(maiorletra_enumero('ABCDDDEEFGHIJKKKKOP'))