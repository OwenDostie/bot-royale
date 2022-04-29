import json
from random import shuffle

class controller:
    def __init__(s):
        s.gamestate = gamestate()
        with open('cards/cards.json') as f:
            j = json.load(f)
            s.cards = [c['name'] for c in j['items']]
            
    def play(s, card):
        s.gamestate.play(card)

    def gs(s):
        return s.gamestate

    def printstate(s):
        s.gamestate.print()

    def findcard(s, card):
        [print(x) for x in s.cards if card in x.lower()]

class gamestate:
    def __init__(s, deck = ['Lumberjack', 'Balloon', 'Elite Barbarians', 'Electro Wizard', 'Snowball', 'Miner', 'Spear Goblins', 'Fireball']):
        shuffle(deck)
        s.my_hand = deck[0:4]
        s.my_deck = deck[4:8]
        s.my_elixer = 8

    def play(s, card):
        if card not in s.my_hand:
            print(f'\n{card} not in hand')
            return 0
        else:
            print(f'\nPlayed {card}')
        s.my_elixer -= 2
        s.my_hand[s.my_hand.index(card)] = s.my_deck.pop()
        s.my_deck.insert(0, card)

    def print(s):
        print(f'\nElixer: {s.my_elixer}\nHand: {s.my_hand}\nDeck: {s.my_deck}')

# load card names from json



# sneak peek at super witch card


# jgkdkdk
# gs = gamestate()


# gs.print()
# gs.play('miner')
# gs.print()