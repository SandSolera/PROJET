from cmath import rect

import core

def Menu():


    core.Draw.text((255, 255, 255), "Asteroide", (core.WINDOW_SIZE[1] / 2 - 100, core.WINDOW_SIZE[1] / 2 - 200))
    core.Draw.text((255, 255, 255), "Appuyer sur espace pour jouer",(core.WINDOW_SIZE[1] / 2 - 230, core.WINDOW_SIZE[1] / 2))
    core.Draw.text((255, 255, 255), "Z : Mise en route réacteur", (core.WINDOW_SIZE[1] / 2 - 200, core.WINDOW_SIZE[1] / 2 + 50))
    core.Draw.text((255, 255, 255), "Q et D : Direction",(core.WINDOW_SIZE[1] / 2 - 200, core.WINDOW_SIZE[1] / 2 + 100))
    core.Draw.text((255, 255, 255), "K et M : Direction Avancé",(core.WINDOW_SIZE[1] / 2 - 200, core.WINDOW_SIZE[1] / 2 + 150))

    if core.getKeyPressList("SPACE"):
        core.memory("etat", 1)
    else:
        pass