def compacta(n): # Usando 'n' como o parâmetro de entrada
    lista = "" # Usando 'lista' para guardar o resultado final
    i = 0      # 'i' será nosso contador de posição (índice)
    while i < len(n):
        caractere_atual = n[i]
        contagem = 1
        
        j = i + 1
        while j < len(n) and n[j] == caractere_atual:
            contagem += 1
            j += 1
            
        lista += caractere_atual
        
        if contagem > 1:
            lista += str(contagem)
            
        # Esta é a parte crucial: atualizamos o 'i' para pular o que já foi contado
        i = j
        
    return lista




def sigla (n):
    lista=''
    nao_pode=['da','do', 'de', 'Para', 'para', 'DE', 'DO', 'DA']
    divisor= n.split(' ')
    for i in divisor:
        if i not in nao_pode:
            lista+=i[0]
    return compacta (lista)

a = input('Digite uma palavra')
print(sigla(a))

