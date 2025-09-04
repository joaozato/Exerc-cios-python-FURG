def encontrar_maior_sequencia(texto):

    # 2. Inicializamos nossas variáveis de controle.
    # A "maior sequência até agora" começa com a primeira letra.
    maior_letra = texto[0]
    maior_contagem = 1

    # A "sequência atual" também começa com a primeira letra.
    letra_atual = texto[0]
    contagem_atual = 1

    # 3. Começamos o loop a partir da SEGUNDA letra (índice 1)
    #    para podermos comparar com a anterior.
    for i in range(1, len(texto)):
        # 4. Compara a letra atual do loop com a letra da sequência que estamos contando
        if texto[i] == letra_atual:
            # Se for igual, a sequência continua. Incrementamos a contagem atual.
            contagem_atual += 1
        else:
            # Se for diferente, a sequência anterior quebrou.
            # Agora, reiniciamos a contagem para a nova letra.
            letra_atual = texto[i]
            contagem_atual = 1

        # 5. Após cada passo, verificamos se a sequência que acabamos de contar
        #    é a maior que já vimos.
        if contagem_atual > maior_contagem:
            maior_contagem = contagem_atual
            maior_letra = letra_atual

    # 6. Retornamos a letra e a contagem da maior sequência encontrada.
    return maior_letra, maior_contagem

# --- Testando a função com o exemplo do exercício ---
print (encontrar_maior_sequencia("ABCDDDEEFGHIJKKKKOP"))