def maior_letra_e_repeticao (texto):
    maior_contagem=1
    maior_letra=texto[0]
    contagem_atual=1
    letra_atual=texto[0]
    for i in range(1, len(texto)):
        if texto[i] == letra_atual:
            contagem_atual+=1
        else:
            letra_atual=texto[i]
            contagem_atual=1
            maior_contagem=contagem_atual
        if contagem_atual > maior_contagem:
            maior_letra=letra_atual
    return 'a maior sequência de letras é de ', maior_letra, 'com',maior_contagem,'incidencias'
            







print(maior_letra_e_repeticao('ABCDDDEEFGHIJKKKKOP'))

