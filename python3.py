#crie uma função que leia a idade e diga se for maior de 18 TRUE e se for menor FALSE

def votacao (idade):
    if idade < 18:
        return False
    else:
        return True
    
print(votacao(21))