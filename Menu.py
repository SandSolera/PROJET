from cmath import rect

import core
from pygame import Vector2


def Menu():


    core.Draw.text((238, 130, 238), "Asteroide", (core.WINDOW_SIZE[1] / 2 - 255, core.WINDOW_SIZE[1] / 2 - 200),100,"Showcard gothic")
    core.Draw.text((255, 255, 255), "Appuyer sur espace pour jouer",(core.WINDOW_SIZE[1] / 2 - 155, core.WINDOW_SIZE[1] / 2-100))
    core.Draw.text((255, 255, 255), "Z : Mise en route réacteur", (core.WINDOW_SIZE[1] / 2 - 200, core.WINDOW_SIZE[1] / 2 + 50))
    core.Draw.text((255, 255, 255), "Q et D : Direction",(core.WINDOW_SIZE[1] / 2 - 200, core.WINDOW_SIZE[1] / 2 + 100))
    core.Draw.text((255, 255, 255), "K et M : Direction Avancé",(core.WINDOW_SIZE[1] / 2 - 200, core.WINDOW_SIZE[1] / 2 + 150))

    if core.getKeyPressList("SPACE"):
        core.memory("etat", 1)
    else:
        pass

    # P1Bis = Vector2(0, 1).rotate(90)
    # P1Bis.scale_to_length(5)
    # P1 = (90, 0) + P1Bis
    #
    # P2Bis = Vector2(0, 1)
    # P2Bis.scale_to_length(20)
    # P2 = (90, 0) + P2Bis
    #
    # P3Bis = Vector2(0, 1).rotate(-90)
    # P3Bis.scale_to_length(5)
    # P3 = (90, 0) + P3Bis
    #
    # core.Draw.polygon((200, 160, 0), (P1, P2, P3))