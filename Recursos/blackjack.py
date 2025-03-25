import Recursos.baralho as deck
#recursos do jogo blackjack
def instacia_jogo(tipo_jogo):
    if (tipo_jogo == 'padrao'):
        baralho_jogador = deck.baralho_comum()
        baralho_banca = deck.baralho_comum()
    elif (tipo_jogo == 'joker'):
        baralho_jogador = deck.baralho_comum()
        baralho_banca = deck.baralho_comum()
    elif (tipo_jogo == 'cassino'):
        baralho_jogador = deck.baralho_comum()
        baralho_banca = deck.baralho_coringa()

    return inicia_jogo(baralho_jogador, baralho_banca)


def pontua(carta, pontuacao):
    if (carta[0].isnumeric()):
        pontuacao = pontuacao + int(carta[0])
        return carta, pontuacao
    elif (carta[0] == "J" or "Q" or "K"):
        pontuacao = pontuacao + 10
        return carta, pontuacao

    elif (carta[0] == "A"):
        if(pontuacao > 11):
            pontuacao = pontuacao + 1
        else:
            pontuacao = pontuacao + 11
        return carta, pontuacao


    elif (carta[0] == "JOKER"):
        if(pontuacao == 11):
            pontuacao = pontuacao + 10
        elif(pontuacao < 11):
            pontuacao = pontuacao + 11
        elif(pontuacao > 11):
            pontuacao = pontuacao + 1
        return carta, pontuacao


def valida_jogo(pontuacao_jogador, pontuacao_banca):
    if (pontuacao_jogador > 21):
        return finalizaJogo(-1)
    elif(pontuacao_banca > 21):
        return finalizaJogo(1)
    elif(pontuacao_banca > pontuacao_jogador):
        return finalizaJogo(-1)
    elif(pontuacao_jogador > pontuacao_banca):
        return finalizaJogo(1)
    elif(pontuacao_banca == pontuacao_jogador):
        return finalizaJogo(0)

def finalizaJogo(resultado):
    if(resultado == 1):
        return "VENCEDOR!"
    elif(resultado == 0):
        return "EMPATE"
    elif(resultado == -1):
        return "PERDEDOR"


def inicia_jogo(baralho_jogador, baralho_banca):
    placar_jogador = 0
    placar_banca = 0
    deck.embaralhar(baralho_jogador)
    deck.embaralhar(baralho_banca)

    return (placar_jogador, baralho_jogador, placar_banca, baralho_banca)

def puxaCarta(baralho, pontuacao):
    return pontua(deck.puxa_carta(baralho), pontuacao)
