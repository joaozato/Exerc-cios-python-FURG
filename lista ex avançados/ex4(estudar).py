'''
4. Substring Única
Implemente uma função `maior_substring_unica(texto)` que encontre a maior substring sem
caracteres repetidos.
Exemplo:
Entrada: "abcabcbb"
Saída: "abc"
Entrada: "bbbbb"
Saída: "b"


'''

'''
def grandona (g):
    lista=[]
    nova=''
    cont=0
    for i in g:
        lista.append(i)
    atual=lista[cont]
    for i in lista:
        if atual in lista:
          nova+=nova +atual
        atual=lista[cont]
        cont+=1
    return atual
    

print(grandona('abcabc'))

'''
'''
def maior_substring_unica_simples(texto):
    """
    Versão mais intuitiva para encontrar a maior substring sem caracteres repetidos.
    """
    maior_substring = ""
    substring_atual = ""
    chars_na_janela = set() # Usamos um conjunto para checagem rápida

    for char in texto:
        # Enquanto o caractere novo já estiver na nossa janela atual...
        while char in chars_na_janela:
            # ...removemos o primeiro caractere da esquerda para abrir espaço.
            char_a_remover = substring_atual[0]
            substring_atual = substring_atual[1:]
            chars_na_janela.remove(char_a_remover)
        
        # Agora que a janela não tem mais o 'char' repetido, podemos adicioná-lo
        substring_atual += char
        chars_na_janela.add(char)
        
        # Verificamos se a substring atual é a nova maior
        if len(substring_atual) > len(maior_substring):
            maior_substring = substring_atual
            
    return maior_substring

# --- Testando a função ---
entrada1 = "abcabcbb"
saida1 = maior_substring_unica_simples(entrada1)
print(f"Entrada: \"{entrada1}\"")
print(f"Saída: \"{saida1}\"")

print("-" * 20)

entrada2 = "pwwkew"
saida2 = maior_substring_unica_simples(entrada2)
print(f"Entrada: \"{entrada2}\"")
print(f"Saída: \"{saida2}\"")

'''


def substring(s):
    a=set()         #o set() armazena caracteres unicos e não repetidos, porém ele não os ordena na ordem de index
    lista=[]        #para isso serve a lista, a lista aqui vai armazenar os que não se repetiram também
    for i in s:      #para i em s 
        if i not in a:   #se i nao estiver em a
            lista.append(i)   #então a lista vai armazenar essa primeira posição, já que ela não esta dentro da organização do set
            a.add(i)     #e o set também vai armazenar essa posição
    return lista                 # o loop repete, até chegar o momento que ele vai repetir novamente essa letra(posição), e como ela ESTÀ dentro do set(), ele não vai armazenar


print(substring('abcabcbb'))