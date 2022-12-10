from pygame import Vector2
from pygame.draw import rect

import core
import time

import random


from Asteroid.Jeu import Jeu
from Asteroid.Menu import Menu
# from Asteroid.Ecran import Menu, Jeu, GameOver
from Asteroid.Target import DrawTarget, Target
from Asteroid.player import DrawPlayer, Controle, Deplacement, BordEcran, Flamme
from Asteroid.projectile import CadenceTir, DrawProj


def setup():

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("pos", Vector2(400, 400))
    core.memory("vitesse", Vector2(1, 0))

    core.memory("Direction", Vector2(1, 0))
    Target()
    core.memory("projectiles", [])
    core.memory("nbtarget",[])
    core.memory("etat",0)

    core.memory("Vie", 3)

def run():

    core.cleanScreen()
    fondecran()

    # Ecran
    if core.memory("etat")==0:
        Menu()
    if core.memory("etat")==1:
        Jeu()
    # if core.memory("etat") == 2:
        # GameOver()

def fondecran():
    core.memory("background", core.Texture("./Espace.png", (1, 1), 0, (800, 800)))

    if not core.memory("background").ready:
        core.memory("background").load()
    core.memory("background").show()
core.main(setup, run)
