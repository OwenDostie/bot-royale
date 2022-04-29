import json

class controller:
    def __init__(s):
        s.gs = gamestate()
        with open('cards/cards.json') as f:
            j = json.load(f)
            s.cards = [c['name'] for c in j['items']]
            
    def play(s, card):
        s.gs.play(card)

    def state(s):
        s.gs.print()

class gamestate:
    def __init__(s):
        s.my_hand = ['miner', 'wallbreakers', 'valk', 'tornado']
        s.my_deck = ['fireball', 'spear gobs', 'bomb tower', 'the log']
        s.my_elixer = 8

    def play(s, card):
        if card not in s.my_hand:
            print(f'{card} not in hand')
            return 0
        else:
            print(f'played {card}')
        s.my_elixer -= 2
        s.my_hand[s.my_hand.index(card)] = s.my_deck.pop()
        s.my_deck.insert(0, card)

    def print(s):
        print(f'''
Elixer: {s.my_elixer}
Hand: {s.my_hand}
Deck: {s.my_deck}
''')

# load card names from json



# sneak peek at super witch card


# jgkdkdk
# gs = gamestate()


# gs.print()
# gs.play('miner')
# gs.print()