def dobrar (n):
    resultado = n * 2
    return resultado

def somacinco (n):
    resultado = n + 5
    return resultado

def final (inicial):
    valordobrado = dobrar(inicial)
    valor_final= somacinco(valordobrado)
    return valor_final

numero_inicial = 10
resultado= final(numero_inicial)
print(f"o resultado final é {resultado}")