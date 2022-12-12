from pygame import *

import core

def GameOver():

    core.Draw.text((255, 255, 255), "! Game Over !", (225,350),50,"Showcard gothic")

    core.Draw.text((255, 255, 255), "Retry", (core.WINDOW_SIZE[1]/2 - 80, 500),50,"Showcard gothic")
    R = Rect((320,500,167,47))
    # core.Draw.rect((255,255,255),(320,500,165,47),1)
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



    core.Draw.text((255, 255, 255), "Menu", (core.WINDOW_SIZE[1]/2 - 70, 550), 50, "Showcard gothic")
    M = Rect((320,550,167,47))
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
