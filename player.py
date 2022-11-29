import core
from pygame.math import Vector2



# Dessin
def DrawPlayer():

    P1Bis = core.memory("vitesse").rotate(90)
    P1Bis.scale_to_length(5)
    P1 = core.memory("pos") + P1Bis

    P2Bis = Vector2(core.memory("vitesse"))
    P2Bis.scale_to_length(20)
    P2 = core.memory("pos") + P2Bis

    P3Bis = core.memory("vitesse").rotate(-90)
    P3Bis.scale_to_length(5)
    P3 = core.memory("pos") + P3Bis

    core.Draw.polygon((0, 0, 255), (P1, P2, P3), 2)

    if core.memory("pos").y < 0:
        core.memory("pos").y = 800

    if core.memory("pos").x < 0:
        core.memory("pos").x = 800

    if core.memory("pos").y > 800:
        core.memory("pos").y = 0

    if core.memory("pos").x > 800:
        core.memory("pos").x = 0