'''

3) (2,5 Pontos) Crie uma função que receba um string com um código HTML e retorne
apenas o texto, retirando assim todas as tags de formatação.



'''



def tiraHTML (html):
    #não consegui tirar todos infelizmente, precisava de mais tempo
    lista=''
    novalista=''
    toma=lista.split()
    malditos=['<','>','/']
    malditos2=['<!DOCTYPE', 'html><html','lang="pt-BR">','<head>','<meta name>="viewport"',
             'content="widht=devide-widht','initial-scale=1.0">','<title>','</title>','</head>','<body>',
             'h1','h1','p','p','a href="https://www.example.com"','</a>','<h2>','</h2>','<img src="imagem.jpg"','alt=',
             '</body></html>']
    for i in html:
        if i not in malditos:
            lista = lista +i
    for i in lista:
        if i not in malditos2:
            novalista= novalista+ i
    return novalista                             







original= '''<!DOCTYPE html><html lang="pt-BR">
<head>
    <meta name="viewport" content="widht=device-width, initial-scale=1.0">
</head>
<body>
    <h1> Bem-vindo à minha página! </h1>
    <p> Este é um paragrafo de exemplo .</p>
    <p> Este é outro parágrafo, com um
    <a href='https://www.example.com">link para um site externo </a>.</p>
    <h2> Uma imagem: </h2>
    <img src='imagem.jpg' alt='uma imagem de exemplo"><body></html>'''

print(tiraHTML(original))
