import interface
import os

c = interface.controller()
gs=c.gs()

while True:
    # read the gamestate
    gs = c.gs()
    h = gs.my_hand
    d = gs.my_deck
    e = gs.my_elixer

    # figure out if it's time
    if ('Balloon' in h) and ('Lumberjack' in h):
        print('It is time.')

    # print gamestate, get input, play card
    c.printstate()
    i = input("Which card do you wanna play? ")
    c.play(i.title())

    # clear output 
    os.system('cls')