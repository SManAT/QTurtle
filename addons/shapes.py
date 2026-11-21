# Shapes, eine Sammlung von Gängigen Polygonen
import math


def nPoly(t, n, r, color=None):
    """generiert ein Polygon mit n Ecken mit Radius r"""
    winkel = 360 / n * math.pi / 180
    mx = t.getX()
    my = t.getY()
    w = 0

    # gehe zum ersten Eckpunkt
    t.teleport(mx + r, my)

    if color is not None:
        t.begin_fill()
    for i in range(n + 1):
        x = mx + r * math.cos(w)
        y = my + r * math.sin(w)
        t.goto(x, y)
        w += winkel
    if color != None:
        t.end_fill()
