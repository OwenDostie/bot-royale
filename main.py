import interface

c = interface.controller()

c.state()

c.play('miner')

c.state()

c.play('wallbreakers')

c.state()

c.play('wallbreakers')

c.state()

[print(x) for x in c.cards if 'Witch' in x]
print(len(c.cards))