import json

# 1. Ler o texto e separar palavra por palavra
try:
    with open('texto.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        # O split separa o texto nos espaços em branco, criando uma lista de palavras
        palavras = conteudo.split()
except FileNotFoundError:
    print("Erro: Crie o arquivo 'texto.txt' primeiro!")
    exit()

# 2. Utilizar um dicionário para dar um código numérico para cada palavra
dicionario_palavras = {}
lista_codigos = []
codigo_atual = 1

for palavra in palavras:
    # Se a palavra ainda não tem código, criamos um novo
    if palavra not in dicionario_palavras:
        dicionario_palavras[palavra] = codigo_atual
        codigo_atual += 1
    
    # 3. O texto original é convertido numa lista de códigos
    # Pegamos o código da palavra e adicionamos na lista final
    codigo_da_palavra = dicionario_palavras[palavra]
    lista_codigos.append(codigo_da_palavra)

print(f"Texto lido: {conteudo}")
print(f"Dicionário criado: {dicionario_palavras}")
print(f"Lista de códigos: {lista_codigos}")

# 4. Armazene em um arquivo o dicionário e a lista
# Vamos criar um "pacote" com os dois dados para salvar
dados_para_salvar = {
    "dicionario": dicionario_palavras,
    "codigos": lista_codigos
}

with open('arquivo_compactado.json', 'w', encoding='utf-8') as arquivo_saida:
    json.dump(dados_para_salvar, arquivo_saida)

print("Arquivo 'arquivo_compactado.json' gerado com sucesso!")