'''

9. Contador de Vogais Únicas
Escreva uma função `vogais_unicas(texto)` que conte quantas vogais distintas aparecem na
string.
Exemplo:
Entrada: "Programacao"
Saída: 3


'''

def vogais_unicas (frase):
    baixo=frase.upper()             #aqui transforma todas as letras da string em maiuscula
    vogais=['A','E','I','O','U','É','Á','Ã','Ô']  #aqui é armazenado uma lista com todas as vogais e suas variantes, (poderia usar chr e ord tbm)
    cont=0     #o contador para contar as vogais
    for i in baixo:   #para i em baixo (a frase com tudo maiusculo para facilitar)
        if i in vogais:  # se i estiver nas vogais (se ele achar uma dessas vogais em cada posição que passar aumenta um contador)
            cont+=1
    return cont   #retorna ele.

print(vogais_unicas('é os guri'))