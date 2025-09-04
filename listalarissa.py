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

'''
n = input('Digite seu voto')
candidatos=[]
while n != 'fim':
    candidatos.append(n)
    n = input('Digite seu voto')

candidatos.sort() #aqui organiza em ordem numérica crescente, mais fácil de contar.
candidato_atual=candidatos[0]    #começando do indice zero
cont_de_votos=1
maior_voto=1
vencedor = candidatos[0]

for i in range (1,len(candidatos)):  #range que vai da posição 1 - até o final do valor len
    if candidatos[i] == candidato_atual:
        cont_de_votos+=1
    else:
        if cont_de_votos > maior_voto:
            maior_voto= cont_de_votos
            vencedor=candidato_atual
        candidato_atual= candidatos[i]
        cont_de_votos=1
print(f'o maior voto é de {vencedor} com {maior_voto} votos')
    
'''

'''

**7-** Mantenha duas listas: produtos e quantidades.

- O programa deve permitir adicionar produto, remover e vender (diminuindo quantidade).
- Se um produto esgotar, deve removê-lo das listas.


'''

produtos = ['Maça', 'Banana','Laranja']
quantidade=[3,2,1]


acao=input('o que você deseja fazer?  \n''Adicionar \n''Remover \n' 'Vender')

while acao != ' ':
    if acao == 'Adicionar':
        np=input('Qual produto você quer adicionar?')
        produtos.append(np)
        qt=int(input('Produto adicionado com sucesso, qual quantidade você quer?'))
        quantidade.append(qt)
        acao=input('o que você deseja fazer?  \n''Adicionar \n''Remover \n' 'Vender')
    if acao == 'Remover':
        print(produtos)
        np=input('Qual produto você quer remover?')
        qt=int(input('Qual quantidade?'))
        remover=produtos.index(np)
        quantidade[remover]-= qt
        if quantidade[remover] <=0:
            produtos.remove(np)
    acao=input('o que você deseja fazer?  \n''Adicionar \n''Remover \n' 'Vender')
    
    if acao == 'Vender':
        np=input('Qual produto você quer vender? ',produtos)
        qt=int(input('Qual quantidade?'))
        acao=input('o que você deseja fazer?  \n''Adicionar \n''Remover \n' 'Vender')
        for np in produtos:
            remover=produtos.index(np)
            quantidade[remover]-= qt
            if quantidade[remover] <=0:
                produtos.remove(np)
    if acao == 'Visualizar':
        print(quantidade,'\n',produtos)
        acao=input('o que você deseja fazer?  \n''Adicionar \n''Remover \n' 'Vender')

