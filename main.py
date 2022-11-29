from pygame import Vector2
from pygame.draw import rect

import core
import time

import random

# from Asteroid.Ecran import Menu, Jeu, GameOver
from Asteroid.Target import DrawTarget
from Asteroid.player import DrawPlayer, Controle, Deplacement
from Asteroid.projectile import CadenceTir, DrawProj


def setup():

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("pos", Vector2(400, 400))
    core.memory("vitesse", Vector2(1, 0))
    core.memory("projectiles", [])
    core.memory("target", (random.randint(0,750), random.randint(0,750), 50, 50))
    core.memory("etat",0)


def run():

    core.cleanScreen()

    # Ecran
    # if core.memory("etat")==0:
    #     Menu()
    # if core.memory("etat")==1:
    #     Jeu()
    # if core.memory("etat")==2:
    #     GameOver()





    # Joueur

    Deplacement()
    Controle()
    DrawPlayer()

    #Projectiles

    CadenceTir()
    DrawProj()
    # Boost()

    #Target

    DrawTarget()
    # Collision()

    #Joueur

    DrawPlayer()



    #CLEAN

    for proj in core.memory("projectiles"):
        if time.time() - proj["startTime"]>10:
            core.memory("projectiles").remove(proj)


core.main(setup, run)
