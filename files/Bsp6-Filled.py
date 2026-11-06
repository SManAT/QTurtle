import colorsys

from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren (bgcolor = Hintergrundfarbe der Grafik)
t = SVGTurtle(width=400, height=400, filename="Bsp6-Filled.svg")
t.speed(0)


def drawPunkte_Lines(P1, P2, P3):
    """Punkte Verbinden"""
    t.pencolor("black")
    t.teleport(P1)
    t.goto(P2)
    t.teleport(P1)
    t.goto(P3)


def schnittpunkt(P1, P2, P3, P4):
    """Schnittpunkt der Geraden P1-P2 und P3-P4"""
    # print(P1)
    # print(P2)
    # print(P3)
    # print(P4)
    x1 = getX(P1)
    x3 = getX(P3)
    y1 = getY(P1)
    y3 = getY(P3)
    y21 = getY(P1 - P2)
    x21 = getX(P1 - P2)
    x34 = getX(P4 - P3)
    y34 = getY(P4 - P3)
    s = (y21 * (x1 - x3) + x21 * (y3 - y1)) / (x34 * y21 - y34 * x21)

    return Punkt(x3 + s * x34, y3 + s * y34)


def printEcken(arr):
    erg = ""
    for e in arr:
        erg += f"P({getX(e):.2f}|{getY(e):.2f}) "
    print(erg)


def drawSchachbrett(P1, P2, P3):
    """Zellen zwischen den Linien abwechselnd schwarz/weiß füllen"""
    n = unterteilungen
    r21 = (P1 - P2) / n
    r31 = (P1 - P3) / n

    def A(i):
        return P2 + r21 * i

    def B(i):
        return P3 + r31 * i

    # Gerade i geht von A(i) nach B(n-i-1)
    # i = -1 ist die x-Achse, i = n die y-Achse
    def X(i, k):
        """Schnittpunkt von Gerade i und Gerade k"""
        return schnittpunkt(A(i), B(n - i - 1), A(k), B(n - k - 1))

    t.pencolor("black")
    for i in range(-1, n):
        for k in range(i + 1, n):
            # Zelle zwischen den Geraden i, i+1 und k, k+1
            ecken = [X(i, k), X(i, k + 1), X(i + 1, k + 1)]
            if k > i + 1:
                ecken.append(X(i + 1, k))  # sonst Dreieck an der Kurve
            printEcken(ecken)

            # Schachbrett: Farbe wechselt mit i + k
            if (i + k) % 2 == 0:
                t.fillcolor("#000000")
            else:
                t.fillcolor("#ffffff")
            t.teleport(ecken[0])
            t.begin_fill()
            for e in ecken[1:]:
                t.goto(e)
            t.goto(ecken[0])
            t.end_fill()


def theL(P1, P2, P3):
    """Zeichne einen Quadranten mit Schachbrettmuster"""
    drawSchachbrett(P1, P2, P3)
    drawPunkte_Lines(P1, P2, P3)


# Hauptprogramm --------------------------------------
if __name__ == "__main__":
    L = 250
    unterteilungen = 3

    # 4 Quadranten, Nachbarn mit vertauschten Farben (versatz 0/1)
    theL(Punkt(0, 0), Punkt(L, 0), Punkt(0, L))
    # theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, L), 1)
    # theL(Punkt(0, 0), Punkt(-L, 0), Punkt(0, -L), 0)
    # theL(Punkt(0, 0), Punkt(L, 0), Punkt(0, -L), 1)

    t.save_svg()
