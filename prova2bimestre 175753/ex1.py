"""
ex 1 jogo da velha

"""


#o que importa é funcionar, e ta funcionando direitinho ta bem
def velha(jogo):
    cont=0
    cont2=0
    for i in jogo:
        if 'X' in jogo[0][0] and 'X' in jogo[1][1] and 'X' in jogo[2][2]:
            return 'x ganhou'
        if 'X' in jogo[0][2] and 'X' in jogo[1][1] and 'X' in jogo[2][0]:
            return 'X ganhou'
        if 'X' in jogo[0][0] and 'X' in jogo[1][0] and 'X' in jogo[2][0]:
            return 'X ganhou'
        if 'X' in jogo[0][1] and 'X' in jogo[1][1] and 'X' in jogo[2][1]:
            return 'X ganhou'
        if 'X' in jogo[0][2] and 'X' in jogo[1][2] and 'X' in jogo[2][2]:
            return 'X ganhou'
        if 'X' in jogo[0][0] and 'X' in jogo[0][1] and 'X' in jogo[0][2]:
            return 'X ganhou'
        if 'X' in jogo[1][0] and 'X' in jogo[1][1] and 'X' in jogo[1][2]:
            return 'X ganhou'
        if 'X' in jogo[2][0] and 'X' in jogo[2][1] and 'X' in jogo[2][2]:
            return 'X ganhou'
        if 'O' in jogo[0][0] and 'O' in jogo[1][1] and 'O' in jogo[2][2]:
            return 'O ganhou'
        if 'O' in jogo[0][2] and 'O' in jogo[1][1] and 'O' in jogo[2][0]:
            return 'O ganhou'
        if 'O' in jogo[0][0] and 'O' in jogo[1][0] and 'O' in jogo[2][0]:
            return 'O ganhou'
        if 'O' in jogo[0][1] and 'O' in jogo[1][1] and 'O' in jogo[2][1]:
            return 'O ganhou'
        if 'O' in jogo[0][2] and 'O' in jogo[1][2] and 'O' in jogo[2][2]:
            return 'O ganhou'
        if 'O' in jogo[0][0] and 'O' in jogo[0][1] and 'O' in jogo[0][2]:
            return 'O ganhou'
        if 'O' in jogo[1][0] and 'O' in jogo[1][1] and 'O' in jogo[1][2]:
            return 'O ganhou'
        if 'O' in jogo[2][0] and 'O' in jogo[2][1] and 'O' in jogo[2][2]:
            return 'O ganhou'
        else:
            return 'Velha'








#xvenceu
tabuleiro1=([['X',' ','O'],
            [' ','X','O'],
            [' ',' ','X']])
#velha
#tabuleiro2=([['X','O','O'],
            #['O','X','X'],
         #   ['X','X','O']])
#
tabuleiro3=([['X',' ','O'],
            ['O',' ','X'],
           ['X','X','O']])
#tabuleiro4=([['O',' ','X'],
       #     [' ','O','X'],
          #  [' ',' ','O']])

#print(tabuleiro1[0][0])
print(velha(tabuleiro3))