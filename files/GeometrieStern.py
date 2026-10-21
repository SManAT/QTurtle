from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren (bgcolor = Hintergrundfarbe der Grafik)
t = SVGTurtle(width=400, height=400, filename="Bsp2_Gerade.svg", bgcolor="white")
t.speed(3)


def drawPunkte_Lines(P1, P2, P3):
    """Punkte Verbinden"""
    t.pencolor("black")
    t.teleport(P1)
    t.goto(P2)
    t.teleport(P1)
    t.goto(P3)


def drawGitter(P1, P2, P3):
    # Richtungsvektoren bestimmen
    r12 = (P2 - P1) / unterteilungen
    r13 = (P1 - P3) / unterteilungen
    # Verbindungen zeichnen
    for i in range(0, unterteilungen):
        # gerade Linien
        t.teleport(P1 + r12 * (i + 1))
        t.goto(P3 + r13 * i)


def drawFlaeche(P1, P2, P3, farbe):
    """Dreieck P1-P2-P3 als farbige Fläche füllen"""
    t.fillcolor(farbe)
    t.begin_fill()
    # Nur goto verwenden: Der Pfad muss lückenlos und geschlossen sein
    t.teleport(P1)
    t.goto(P2)
    t.goto(P3)
    t.goto(P1)
    t.end_fill()


def theL(P1, P2, P3, farbe):
    """Zeichne einen Quadranten mit den Vektorlinien"""
    # Erst die Fläche, dann die Linien darüber
    drawFlaeche(P1, P2, P3, farbe)
    drawPunkte_Lines(P1, P2, P3)
    drawGitter(P1, P2, P3)


# Hauptprogramm --------------------------------------
if __name__ == "__main__":
    L = 250
    unterteilungen = 40
    # 4 Quadranten, jeweils mit eigener Farbe
    theL(Punkt(0, 0), Punkt(0, L), Punkt(L, 0), "cornflowerblue")
    theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, L), "mediumseagreen")
    theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, -L), "lightcoral")
    theL(Punkt(0, 0), Punkt(L, 0), Punkt(0, -L), "gold")

    t.save_svg()
