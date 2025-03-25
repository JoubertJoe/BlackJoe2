#Definindo Baralho(s)
import pyCardDeck
import pyCardDeck as deck

# lista de Naipes
Naipes = ['PAUS', 'OURO',
         'CORACAO', 'ESPADA']
# lista de ranks
Ranks = ['A', '2', '3', '4',
         '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K']

def baralho_comum():
    #Retorna o baralho Padrao
    baralho = []
    for rank in Ranks:

        for naipe in Naipes:
            carta = [rank, naipe]
            baralho.append(carta)


    baralho = pyCardDeck.Deck(cards = baralho, name= "Baralho Comum")
    return baralho

def baralho_coringa():
    
    baralho = []
    for rank in Ranks:

        for naipe in Naipes:
            carta = [rank, naipe]
            baralho.append(carta)
    
    baralho.append(["JOKER", "PRETO"])
    baralho.append(["JOKER", "VERMELHO"])

    baralho = pyCardDeck.Deck(cards=baralho, name="Baralho Comum")
    return baralho

print(baralho_coringa().json)



