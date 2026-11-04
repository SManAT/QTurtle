import colorsys
import math

from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren (bgcolor = Hintergrundfarbe der Grafik)
t = SVGTurtle(width=400, height=400, filename="Bsp5_Quadrate.svg")
t.speed(0)


def toRad(w):
    return w * math.pi / 180


def regenbogen(anteil):
    """Farbe aus dem Farbkreis: anteil 0.0 = rot ... 1.0 = wieder rot"""
    r, g, b = colorsys.hsv_to_rgb(anteil % 1.0, 1.0, 0.9)
    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))


def singleQuadrate(L):
    """Zeichne immer kleiner werdende Quadrate"""
    # Eckpunkte
    P1 = Punkt(L / 2, 0)
    P2 = Punkt(L / 2, L / 2)
    P3 = Punkt(-L / 2, L / 2)
    P4 = Punkt(-L / 2, -L / 2)
    P5 = Punkt(L / 2, -L / 2)
    t.teleport(P1)
    t.goto(P2)
    t.goto(P3)
    t.goto(P4)
    t.goto(P5)
    t.goto(P1)


def theQuadrate(L, unterteilungen):
    """Zeichne immer kleiner werdende Quadrate"""
    for i in range(0, unterteilungen):
        singleQuadrate(L)
        L *= 1 - i / unterteilungen


def theLines(L, unterteilungen):
    """Zeichne immer kleiner werdende Quadrate"""
    delta_winkel = 360 / unterteilungen
    winkel = 0
    for i in range(0, unterteilungen):
        t.teleport(0, 0)
        t.setheading(winkel)
        # mit Pythagoras Länge berechnen
        if 0 <= winkel <= 45 or 135 <= winkel <= 225 or 315 <= winkel <= 360:
            t.forward(L / 2 / abs(math.cos(toRad(winkel))))
        else:
            t.forward(L / 2 / abs(math.sin(toRad(winkel))))
        winkel += delta_winkel


# Hauptprogramm --------------------------------------
if __name__ == "__main__":
    L = 400
    unterteilungen = 40

    # 4 Quadranten, jeweils mit eigener Farbe
    theQuadrate(L, unterteilungen)
    # Gitterlinien
    theLines(L, unterteilungen)

    t.save_svg()
