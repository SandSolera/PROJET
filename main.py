from pygame import Vector2
from pygame.draw import rect

import core
import time

import random

from Asteroide.player import DrawPlayer
from Asteroide.projectile import projectiles


def setup():

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("pos", Vector2(400, 400))
    core.memory("vitesse", Vector2(1, 0))
    core.memory("projectiles", [])
    core.memory("target", (random.randint(0,750), random.randint(0,750), 50, 50))
def run():

    core.cleanScreen()

    #Control

    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length()+0.5)

    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(10))

    if core.getKeyPressList("q"):
        core.memory("vitesse", core.memory("vitesse").rotate(-10))

    if core.getKeyPressList("SPACE"):

        if len(core.memory("projectiles"))>0:
            if time.time()-core.memory("projectiles")[-1]["startTime"] > 1:
                projectiles()
        else:
            projectiles()


    #Deplacement

    core.memory("pos", core.memory("pos") + core.memory("vitesse"))

    #Projectiles
    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["couleur"],proj["position"],proj["rayon"])

    for proj in core.memory("projectiles"):
        proj["position"]=proj["position"]+proj["vitesse"]

    #Target
    core.Draw.rect((255, 0, 0), core.memory("target"))


    #Dessin

    DrawPlayer()



    #CLEAN

    for proj in core.memory("projectiles"):
        if time.time() - proj["startTime"]>10:
            core.memory("projectiles").remove(proj)


core.main(setup, run)
