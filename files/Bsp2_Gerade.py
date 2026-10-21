from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="Bsp2_Gerade.svg")
t.speed(3)


def drawPunkte_Lines(P1, P2, P3):
    """Punkte Verbinden"""
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


def theL(P1, P2, P3):
    """Zeichne einen Qudranten mit den Vektorlinien"""
    drawPunkte_Lines(P1, P2, P3)
    drawGitter(P1, P2, P3)


# Hauptprogramm --------------------------------------
if __name__ == "__main__":
    L = 250
    unterteilungen = 40
    # 1 Quadrant
    theL(Punkt(0, 0), Punkt(0, L), Punkt(L, 0))
    theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, L))
    theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, -L))
    theL(Punkt(0, 0), Punkt(L, 0), Punkt(0, -L))

    t.save_svg()
