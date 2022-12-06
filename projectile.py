import core
import time
from pygame.math import Vector2

def projectiles():
    p = Vector2(core.memory("pos"))
    v=Vector2(core.memory("Direction"))
    v.scale_to_length(core.memory("vitesse").length()+5)
    r=5
    c=(255,255,255)
    st=time.time()

    d = {"position": p, "vitesse": v, "rayon": r, "couleur": c, "startTime": st}
    core.memory("projectiles").append(d)

def CadenceTir():

    if core.getKeyPressList("SPACE"):

        if len(core.memory("projectiles"))>0:
            if time.time()-core.memory("projectiles")[-1]["startTime"] > 1:
                projectiles()
        else:
            projectiles()

def DrawProj():

    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["couleur"],proj["position"],proj["rayon"])

    for proj in core.memory("projectiles"):
        proj["position"]=proj["position"]+proj["vitesse"]