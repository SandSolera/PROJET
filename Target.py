import core
from pygame.draw import rect
import random

def Target():

    x = random.randint(0, 750)
    y = random.randint(0, 750)
    l = 50
    h = 50

    core.memory("target", (x, y, l, h))

    core.Draw.rect((255, 0, 0), core.memory("target"))

def DrawTarget():

    core.Draw.rect((255, 0, 0), core.memory("target"))