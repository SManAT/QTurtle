from qturtle_app.svg_turtle_class import SVGTurtle

import math

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="Primzahlkreis.svg")
t.color("green")
t.speed(8)


def getPunkt(b, n, p):
    """Punkt am Kreis gemäß Anleitung berechnen"""
    winkel = 2 * math.pi * x_pow_y_mod_n(b, n, p) / n
    x = radius * math.cos(winkel)
    y = radius * math.sin(winkel)
    return [x, y]


p = 569
radius = 200
b = 19

t.circle([0, 0], radius)

# Kreispunkte berechnen ---------

# Erste Punkt
P1 = getPunkt(b, 1, p)
for n in range(2, p - 1):
    # NachfolgePunkt berechnen
    P2 = getPunkt(b, n, p)
    t.teleport(P1)
    t.goto(P2)
    # neuen Startpunkt setzen
    P1 = P2
# letzter Punkt wieder zum Anfang
t.teleport(P1)
t.goto(getPunkt(b, 1, p))


t.save_svg()
