from pygame import *

import core

def GameOver():

    core.Draw.text((255, 255, 255), "GameOver", (325,350))

    core.Draw.text((255, 255, 255), "Retry", (350, 500))
    R = Rect((340,500,100,50))

    if core.getMouseLeftClick():
        if R.collidepoint(core.getMouseLeftClick()):
            core.memory("etat", 1)
            core.memory("pos", Vector2(400, 400))
            core.memory("vitesse", Vector2(1, 0))
            core.memory("Direction", Vector2(1, 0))
            core.memory("target", [])
            core.memory("projectiles", [])
            core.memory("temps", [])
            core.memory("difficulte", 1)
            core.memory("Vie", 3)
            core.memory("point", 0)
            core.memory("timer", 0)
            core.memory("Tdiff", 30)



    core.Draw.text((255, 255, 255), "Menu", (350, 550), 120)
    M = Rect((340, 550, 100, 50))
    if core.getMouseLeftClick():
        if M.collidepoint(core.getMouseLeftClick()):
            core.memory("etat", 0)
            core.memory("pos", Vector2(400, 400))
            core.memory("vitesse", Vector2(1, 0))
            core.memory("Direction", Vector2(1, 0))
            core.memory("target", [])
            core.memory("projectiles", [])
            core.memory("temps", [])
            core.memory("difficulte", 1)
            core.memory("Vie", 3)
            core.memory("point", 0)
            core.memory("timer", 0)
            core.memory("Tdiff", 30)

    core.Draw.text((255, 255, 255), "Score :", (100, 100))
    core.Draw.text((255, 255, 255), str(core.memory("point")), (205, 100))

    core.Draw.text((255, 255, 255), "Temps resté en vie :", (420, 100))
    core.Draw.text((255, 255, 255), str(int(core.memory("timer"))), (705, 100))
