import time

import core

from Asteroid.Difficulté import difficulte
from Asteroid.Target import DrawTarget, collisionproj, CreationTarget, BordEcranTarget, collisionplayer, reset
from Asteroid.Vie import Vie
from Asteroid.player import Deplacement, Controle, DrawPlayer, BordEcranPlayer
from Asteroid.projectile import CadenceTir, DrawProj, SupprProj, BordEcranProj


def Jeu():
    # if core.memory("etat",1):

    #Affichage

    core.Draw.text((255, 255, 255), "Score : ",(0,0),15)
    core.Draw.text((255, 255, 255), str(core.memory("point")), (105, 0),15)
    core.Draw.text((255, 255, 255), "Temps : ", (200,0), 15)
    core.Draw.text((255,255,255),str(int(core.memory("timer"))),(315,0), 15)
    core.Draw.text((255, 255, 255), "Vies restantes : ", (400, 0), 15)

    Vie()


    # Joueur

    Deplacement()
    Controle()
    DrawPlayer()
    BordEcranPlayer()

    # Projectiles

    CadenceTir()
    DrawProj()
    SupprProj()
    BordEcranProj()

    # Boost()


    # Target

    DrawTarget()
    CreationTarget()
    collisionproj()
    BordEcranTarget()
    collisionplayer()



    #Difficulté

    difficulte()

    if core.memory("Vie") == 0:
        core.memory("etat", 2)

    if core.getKeyPressList("ESCAPE"):
        core.memory("etat, 0")



