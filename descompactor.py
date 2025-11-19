import json

# 1. Ler o arquivo compactado e extrair a lista e o dicionário
try:
    with open('arquivo_compactado.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        
    dicionario = dados["dicionario"]
    lista_codigos = dados["codigos"]
except FileNotFoundError:
    print("Erro: Rode o compactador primeiro!")
    exit()

# Precisamos inverter o dicionário.
# O original é {"palavra": 1}, mas para descompactar precisamos de {1: "palavra"}
dicionario_invertido = {}
for palavra, codigo in dicionario.items():
    dicionario_invertido[codigo] = palavra

# 2. Para cada código, converta na palavra equivalente
palavras_recuperadas = []

for codigo in lista_codigos:
    # O dicionário original salvou chaves como strings no JSON, mas nossos códigos na lista são int.
    # Por segurança, garantimos que estamos buscando a mesma coisa.
    palavra = dicionario_invertido[codigo]
    palavras_recuperadas.append(palavra)

# Juntamos as palavras de volta com um espaço entre elas
texto_final = " ".join(palavras_recuperadas)

print(f"Texto recuperado: {texto_final}")

# 3. Salve a lista de palavras em um arquivo
with open('texto_descompactado.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(texto_final)

print("Arquivo 'texto_descompactado.txt' criado com sucesso!")