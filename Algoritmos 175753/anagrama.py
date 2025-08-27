def anagrama(txt1, txt2):
    lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for letra in txt1:
        indice = ord(letra) - 65
        lista[indice] += 1

    for letra in txt2:
        indice = ord(letra) - 65
        lista[indice] -= 1

    for num in lista:
        if num != 0:
            return False
    return True

anagrama('Roma','Amor')