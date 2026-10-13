from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="Bsp2.svg")
t.speed(3)

P1 = Punkt(0, 0)
P2 = Punkt(0, 300)
P3 = Punkt(300, 0)


def drawPunkte_Lines():
    """Punkte Verbinden"""
    t.penup()
    t.goto(P1)
    t.pendown()
    t.goto(P2)
    t.penup()
    t.goto(P1)
    t.pendown()
    t.goto(P3)
    
def drawGitter():
    # Richtungsvektoren bestimmen
    unterteilungen = 20
    r12 = vektor_mal(P2 - P1, 1 / unterteilungen)
    r13 = vektor_mal(P3 - P1, 1 / unterteilungen)
    # Verbindungen zeichnen

    for i in range(0, unterteilungen):
        # Bezierkurven
        Q1=vektor_add(P1, vektor_mal(r12, i+1))
        Q2=vektor_add(P3, vektor_mal(r13, -1 * i))
        
        points = getBezierPunkte(Q1, P1, Q2, 50)
        first=True
        for data in points:
            if first:
                t.teleport(data)
                first=False
            else:
                t.goto(data)
        
        #bezier(P1, Q1, Q2, 40)
        # gerade Linien
        # t.teleport(vektor_add(P1, vektor_mal(r12, i+1)))
        # t.goto(vektor_add(P3, vektor_mal(r13, -1 * i)))


# Hauptprogramm --------------------------------------
drawPunkte_Lines()
drawGitter()

t.save_svg()
