from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="Bsp2_Gerade.svg")
t.speed(3)

P1 = Punkt(0, 0)
P2 = Punkt(0, 300)
P3 = Punkt(300, 0)


def drawPunkte_Lines():
    """Punkte Verbinden"""
    t.teleport(P1)
    t.goto(P2)
    t.teleport(P1)
    t.goto(P3)


def drawGitter():
    # Richtungsvektoren bestimmen
    unterteilungen = 40
    r12 = (P2 - P1) / unterteilungen
    r13 = (P1 - P3) / unterteilungen
    # Verbindungen zeichnen
    for i in range(0, unterteilungen):
        # gerade Linien
        t.teleport(P1 + r12 * (i + 1))
        t.goto(P3 + r13 * i)


# Hauptprogramm --------------------------------------
drawPunkte_Lines()
drawGitter()

t.save_svg()
