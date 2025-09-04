'''
2. Estatísticas de Texto
Crie uma função `estatisticas_texto(texto)` que receba uma string e retorne uma lista com:
- número de palavras,
- número de caracteres,
- tamanho médio das palavras,
- a palavra mais longa.
Exemplo:
Entrada: "Python é divertido"
Saída:
[['palavras', 'caracteres', 'tamanho_medio', 'mais_longa'], [3, 17, 5.6, 'divertido'}]]
'''

def estatisticas_texto(texto):
    a = texto.split()
    cont2=0
    tamanho=[]
    media=0
    maxima=max(a, key=len)#retorna a maior palavra
    quantidade_palavras=len(a)#contador de palavras
    caracteres=len(texto)#conta a quantidade de caracteres
    for i in a:
        tamanho.append((len(a[cont2])))
        cont2+=1
    for i in tamanho:
        media+=i
    media=round((media/len(tamanho)),2)#aqui ele faz a média
    return 'a string tem', quantidade_palavras,'palavras', caracteres,'caracteres e um tamanho médio de ',media,' e a maior palavra é ',maxima

print(estatisticas_texto('Python é divertido'))




        


