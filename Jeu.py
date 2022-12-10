import time

import core
from Asteroid.Target import DrawTarget
from Asteroid.player import Deplacement, Controle, DrawPlayer, BordEcran
from Asteroid.projectile import CadenceTir, DrawProj, SupprProj


def Jeu():
    # if core.memory("etat",1):
    #
    # Joueur

    Deplacement()
    Controle()
    DrawPlayer()
    BordEcran()

    # Projectiles

    CadenceTir()
    DrawProj()
    SupprProj()

    # Boost()


    # Target


    DrawTarget()
    # Collision()

    # Joueur

    DrawPlayer()



