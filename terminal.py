import Recursos.blackjack as bj
from pprint import pprint
import inquirer

from Recursos.baralho import embaralhar

modo_jogo = [
    inquirer.List(
        "modo_jogo",
        message="Qual Modo você quer jogar",
        choices=["padrao", "joker", "cassino"],
    ),
]

numero_cartas = [
    inquirer.List(
        "revelar",
        message= "Quantas cartas você quer revelar?",
        choices= [1, 2, 3],
    ),
]

def mostrar_carta(carta):
    rank = carta[0]
    naipe = carta[1]

    if(naipe == "ESPADA"):
        naipe = "♠"
    elif (naipe == "CORACAO"):
        naipe = "♥"
    elif (naipe == "PAU"):
        naipe = "♣"
    elif (naipe == "OURO"):
        naipe = "♦"

    print("[" + naipe + "-"+ rank + "]")





def modoDeJogo():
    modo = inquirer.prompt(modo_jogo)
    modo = modo["modo_jogo"]

    if ((modo == "padrao") or (modo == "joker") or (modo == "cassino")):
        return bj.instacia_jogo(modo)
    else:
        modoDeJogo()

def jogador_puxar_carta(qtd, pontuacao_total, baralho_jogador):
    for i in range(qtd):
        carta, pontuacao = bj.puxaCarta(baralho_jogador, placar_jogador)
        mostrar_carta(carta)
        pontuacao_total = pontuacao_total + pontuacao
    return pontuacao_total


def vez_jogador(placar_jogador, baralho_jogador):
    qtd_cartas = inquirer.prompt(numero_cartas)
    qtd_cartas = qtd_cartas["revelar"]
    placar_jogador = jogador_puxar_carta(qtd_cartas, placar_jogador, baralho_jogador)
    if (placar_jogador <= 21):
        print("Seu placar Atual: ", placar_jogador)
    else:
        print("Sinto muito mas você estorou o placar!")
        print("Total : ", placar_jogador)

    return placar_jogador

def vez_banca(placar_banca, baralho_banca, placar_jogador):
    while((placar_banca < 17) or (placar_banca < placar_jogador)):
        carta, placar_banca = bj.puxaCarta(baralho_banca, placar_banca)
        mostrar_carta(carta)
        print("Placar Banca: ", placar_banca)
    return placar_banca



print("Main Test")
placar_jogador, baralho_jogador, placar_banca, baralho_banca = modoDeJogo()
print("O jogo começou")
print("Placar Jogador :", placar_jogador)
print("Placar Banca :", placar_banca)

print("Embaralhando")
print("Você começa:")
placar_jogador = vez_jogador(placar_jogador, baralho_jogador)
if (placar_jogador < 21):
    placar_banca = vez_banca(placar_banca, baralho_banca, placar_jogador)
print(bj.valida_jogo(placar_jogador, placar_banca))