import colorsys

from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren (bgcolor = Hintergrundfarbe der Grafik)
t = SVGTurtle(width=400, height=400, filename="Bsp2_GeometrieStern.svg")
t.speed(3)


def drawPunkte_Lines(P1, P2, P3):
    """Punkte Verbinden"""
    t.pencolor("black")
    t.teleport(P1)
    t.goto(P2)
    t.teleport(P1)
    t.goto(P3)


def regenbogen(anteil):
    """Farbe aus dem Farbkreis: anteil 0.0 = rot ... 1.0 = wieder rot"""
    r, g, b = colorsys.hsv_to_rgb(anteil % 1.0, 1.0, 0.9)
    return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))


def drawGitter(P1, P2, P3):
    # Richtungsvektoren bestimmen
    r12 = (P2 - P1) / unterteilungen
    r13 = (P1 - P3) / unterteilungen
    # Verbindungen zeichnen
    for i in range(0, unterteilungen):
        # jede Linie bekommt ihre eigene Regenbogenfarbe
        t.pencolor(regenbogen(i / unterteilungen))
        # gerade Linien
        t.teleport(P1 + r12 * (i + 1))
        t.goto(P3 + r13 * i)


def theL(P1, P2, P3):
    """Zeichne einen Quadranten mit den Vektorlinien"""
    # Erst die Fläche, dann die Linien darüber
    drawPunkte_Lines(P1, P2, P3)
    drawGitter(P1, P2, P3)


# Hauptprogramm --------------------------------------
if __name__ == "__main__":
    L = 250
    unterteilungen = 40
    # 4 Quadranten, jeweils mit eigener Farbe
    theL(Punkt(0, 0), Punkt(0, L), Punkt(L, 0))
    theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, L))
    theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, -L))
    theL(Punkt(0, 0), Punkt(L, 0), Punkt(0, -L))

    t.save_svg()
