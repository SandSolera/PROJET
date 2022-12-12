from pygame import Vector2

import core
def Vie():
    if core.memory("Vie")==3:
        P1Bis = Vector2(0,-1).rotate(90)
        P1Bis.scale_to_length(5)
        P1 = (90,130) + P1Bis

        P2Bis = Vector2(0,-1)
        P2Bis.scale_to_length(20)
        P2 = (90,130) + P2Bis

        P3Bis = Vector2(0,-1).rotate(-90)
        P3Bis.scale_to_length(5)
        P3 = (90,130) + P3Bis

        P4Bis = Vector2(0, -1).rotate(90)
        P4Bis.scale_to_length(5)
        P4 = (110, 130) + P4Bis

        P5Bis = Vector2(0, -1)
        P5Bis.scale_to_length(20)
        P5 = (110, 130) + P5Bis

        P6Bis = Vector2(0, -1).rotate(-90)
        P6Bis.scale_to_length(5)
        P6 = (110, 130) + P6Bis

        P7Bis = Vector2(0, -1).rotate(90)
        P7Bis.scale_to_length(5)
        P7 = (130, 130) + P7Bis

        P8Bis = Vector2(0, -1)
        P8Bis.scale_to_length(20)
        P8 = (130, 130) + P8Bis

        P9Bis = Vector2(0, -1).rotate(-90)
        P9Bis.scale_to_length(5)
        P9 = (130, 130) + P9Bis

        core.Draw.polygon((200, 160, 0), (P1, P2, P3))
        core.Draw.polygon((200, 160, 0), (P4, P5, P6))
        core.Draw.polygon((200, 160, 0), (P7, P8, P9))

    if core.memory("Vie") == 2:
        P1Bis = Vector2(0, -1).rotate(90)
        P1Bis.scale_to_length(5)
        P1 = (90,130) + P1Bis

        P2Bis = Vector2(0, -1)
        P2Bis.scale_to_length(20)
        P2 = (90,130) + P2Bis

        P3Bis = Vector2(0, -1).rotate(-90)
        P3Bis.scale_to_length(5)
        P3 = (90,130) + P3Bis

        P4Bis = Vector2(0, -1).rotate(90)
        P4Bis.scale_to_length(5)
        P4 = (650, 28) + P4Bis

        P5Bis = Vector2(0, -1)
        P5Bis.scale_to_length(20)
        P5 = (110, 130) + P5Bis

        P6Bis = Vector2(0, -1).rotate(-90)
        P6Bis.scale_to_length(5)
        P6 = (110, 130) + P6Bis

        core.Draw.polygon((200, 160, 0), (P1, P2, P3))
        core.Draw.polygon((200, 160, 0), (P4, P5, P6))

    if core.memory("Vie") == 1:
        P1Bis = Vector2(0, -1).rotate(90)
        P1Bis.scale_to_length(5)
        P1 = (90,130) + P1Bis

        P2Bis = Vector2(0, -1)
        P2Bis.scale_to_length(20)
        P2 = (90,130) + P2Bis

        P3Bis = Vector2(0, -1).rotate(-90)
        P3Bis.scale_to_length(5)
        P3 = (90,130) + P3Bis

        core.Draw.polygon((200, 160, 0), (P1, P2, P3))