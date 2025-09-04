def incidencias(palavras):
    lista=[[x, palavras.count(x)] for x in set(palavras)]
    return lista

print(incidencias(["maçã", "banana", "maçã", "laranja", "banana", "maçã"]))
    