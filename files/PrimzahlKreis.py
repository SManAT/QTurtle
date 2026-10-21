import math

from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="Primzahlkreis.svg")
t.color("green")
t.speed(8)


def getPunkt(b, n, p):
    """Punkt am Kreis gemäß Anleitung berechnen"""
    winkel = 2 * math.pi * x_pow_y_mod_n(b, n, p) / n
    x = radius * math.cos(winkel)
    y = radius * math.sin(winkel)
    return Punkt(x, y)


def rgb_to_hex(rgb):
    return "#{0:02x}{1:02x}{2:02x}".format(*rgb)


def bunteLinie(P1, P2):
    FARBEN = [
        (20, 20, 50),
        (120, 120, 150),
        (220, 220, 250),
        (200, 200, 150),
        (250, 250, 100),
        (100, 100, 150),
        (100, 100, 100),
        (20, 120, 150),
        (20, 200, 200),
        (160, 200, 250),
    ]
    vec = (P2 - P1) / 10

    Pm = P1
    # Linie in 10 verschiedenen Farben unterteilen
    for j in range(1, 11):

        P2 = P1 + j * vec
        t.pencolor(rgb_to_hex(FARBEN[j - 1]))
        t.teleport(Pm)
        t.goto(P2)
        Pm = P2


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
    # t.teleport(P1)
    # t.goto(P2)
    bunteLinie(P1, P2)

    # neuen Startpunkt setzen
    P1 = P2
# letzter Punkt wieder zum Anfang
t.teleport(P1)


t.goto(getPunkt(b, 1, p))


t.save_svg()
