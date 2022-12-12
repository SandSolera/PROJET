import time

import core

def difficulte() :

    print(core.memory("timer"), core.memory("temps"))
    print(core.memory("difficulte"))


    if core.memory("etat") == 1:
        t = time.time()
        core.memory("temps").append(t)
        core.memory("timer", time.time() - core.memory("temps")[0])
        if len(core.memory("temps"))>2:
            core.memory("temps").pop()

        core.memory("Tdiff")
        if core.memory("timer") >= core.memory("Tdiff") :
            core.memory("difficulte", core.memory("difficulte") + 1 )
            core.memory("Tdiff", core.memory("Tdiff") + 30)