import core
from pygame.math import Vector2



    # Dessin



def Flamme():

    f1 = core.memory("Direction").rotate(180)
    f1.scale_to_length(8)
    F1 = core.memory("pos") + f1

    f2 = core.memory("Direction").rotate(90)
    f2.scale_to_length(-5)
    F2 = core.memory("pos") + f2

    f3 = core.memory("Direction").rotate(-90)
    f3.scale_to_length(-5)
    F3 = core.memory("pos") + f3

    core.Draw.polygon((255, 0, 0), (F1, F2, F3), 2)

def DrawPlayer():

    P1Bis = core.memory("Direction").rotate(90)
    P1Bis.scale_to_length(5)
    P1 = core.memory("pos") + P1Bis

    P2Bis = Vector2(core.memory("Direction"))
    P2Bis.scale_to_length(20)
    P2 = core.memory("pos") + P2Bis

    P3Bis = core.memory("Direction").rotate(-90)
    P3Bis.scale_to_length(5)
    P3 = core.memory("pos") + P3Bis

    core.Draw.polygon((0, 0, 255), (P1, P2, P3), 2)

    # Contrôle

def Controle():
    Vmax = 20
    Vmin = 0.5
    print(core.memory("vitesse"))
    if core.getKeyPressList("z"):
        if core.memory("vitesse").x <= Vmax and core.memory("vitesse").x >= -Vmax and core.memory("vitesse").y <= Vmax and core.memory("vitesse").y >= -Vmax:
                core.memory("vitesse").scale_to_length(core.memory("vitesse").length()+0.2)
        core.memory("vitesse", core.memory("Direction"))
        Flamme()
    else :
        if core.memory("vitesse").x >= Vmin or core.memory("vitesse").x <= -Vmin and core.memory("vitesse").y >= Vmin or core.memory("vitesse").y <= -Vmin:

                core.memory("vitesse").scale_to_length(core.memory("vitesse").length() - 0.4 )


    if core.getKeyPressList("d"):
        core.memory("Direction", core.memory("Direction").rotate(10))

    if core.getKeyPressList("q"):
        core.memory("Direction", core.memory("Direction").rotate(-10))


# Passage par le bord de l'écran

def BordEcran():
    if core.memory("pos").y < 0:
        core.memory("pos").y = core.WINDOW_SIZE[1]

    if core.memory("pos").x < 0:
        core.memory("pos").x = core.WINDOW_SIZE[1]

    if core.memory("pos").y > core.WINDOW_SIZE[1]:
        core.memory("pos").y = 0

    if core.memory("pos").x > core.WINDOW_SIZE[1]:
        core.memory("pos").x = 0

def Deplacement():
    core.memory("pos", core.memory("pos") + core.memory("vitesse"))