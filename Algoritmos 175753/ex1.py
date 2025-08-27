'''
1- Dada uma lista de strings, crie um programa que retorne apenas as que são palíndromos (iguais de frente pra trás).



'''
'''

p = ['ana', 'tenet','arara','luiz']
palindromos=[]
for i in p:
    if i == i[::-1]:
        palindromos.append(i) 
print(palindromos)






'''
'''

 Implemente um programa que recebe uma string e um número N e desloca cada letra do texto N posições 
no alfabeto (ex: "abc", 2 → "cde"). Se passar do "z", deve voltar para o "a”.
'''

'''
frase=input('Digite ai')
n=int(input('digita a merda do numero'))
aumentado=''
for i in frase:
    a = (ord(i) +n)
    if a > 122:
        a -= 26
    aumentado = aumentado+chr(a)
print(aumentado)

'''
'''

**3-** Dada uma lista de palavras, agrupe as que são anagramas (mesmas letras em ordem diferente). Exemplo:

Entrada →["amor", "roma", "carro", "roca", "arco"]

Saída →[["amor", "roma"], ["carro"], ["roca", "arco"]]



'''
'''
entrada=["amor", "roma", "carro", "roca", "arco"]

'''


'''

**4-** Peça uma senha e verifique se ela é válida segundo as regras:

- Pelo menos 8 caracteres
- Contém pelo menos uma letra maiúscula, uma minúscula e um número
- Não pode ter espaços

'''
'''
senha= input('digite a senha')
if len(senha) >= 8 and ' ' not in senha:
    tamanho=True
    maiuscula = False
    minuscula = False
    numero= False
    for x in senha:
        if maiuscula == False and ord(x) in range(65, 91):
            maiuscula= True
        if minuscula == False and ord(x) in range(97, 123):
            minuscula = True
        if numero == False and ord(x) in range(48,58):
            numero = True
    if maiuscula == True and minuscula == True and tamanho == True and numero == True:
        print('A senha é correta')
    else:
        print ('senha incorreta')


'''
'''



**6-** Faça um sistema de votação. O programa deve:

- Pedir votos (número do candidato) em loop até digitar "fim"
- Mostrar o candidato vencedor (ou empate) ao final




'''
n = ''


    