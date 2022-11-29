import core
import time
from pygame.math import Vector2

def projectiles():
    p = Vector2(core.memory("pos"))
    v=Vector2(core.memory("vitesse"))
    v.scale_to_length(core.memory("vitesse").length()+5)
    r=5
    c=(255,255,255)
    st=time.time()

    d = {"position": p, "vitesse": v, "rayon": r, "couleur": c, "startTime": st}
    core.memory("projectiles").append(d)
