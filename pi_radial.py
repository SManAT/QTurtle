from SVG_Turtle import SVG_Turtle
import math


def getWinkel(ziffer):
    """get Winkel per Ziffer 10 = 360°"""
    return 360 / 10 * ziffer


def main():
    params = {"title": "Pi Radial", "filename": "PiRadial.svg", "size": (500, 500)}
    t = SVG_Turtle(params)
    t.speed(8)

    pi = "3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273"
    stellen = 32
    radius = 14
    deltaR = 8
    komma_radius = radius / 15
    fill_color = "#000000"

    # Mittelpunkt
    t.createFilledCircle(0, 0, fill_color, radius, 360, 50)
    t.left(90)
    t.penup()
    t.forward(2 * radius)
    t.pendown()
    t.forward(deltaR)
    t.right(90)

    radius = radius + deltaR
    start_winkel = 90
    # Kommapunkt Flag
    first = True
    for i in range(stellen):
        char = pi[i]
        # print(char)
        if char != "." and char != " ":
            winkel = -1 * int(char) * 36
            t.drawArc(0, 0, radius, start_winkel, winkel)

            x, y = t.pos()
            heading = t.outsideHeading(x, y)
            t.setheading(heading)

            t.forward(deltaR)
            radius += deltaR
            start_winkel += winkel
        if first:
            # Kommapunkt zeichnen, in Verlängerung des ersten Kreisbogens
            t.penup()
            x, y = t.getPosviaAngle(radius - deltaR, start_winkel * 1.4)
            t.createFilledCircle(x, y, fill_color, komma_radius, 360, 50)
            first = False
            # Turtle zurücksetzen
            t.penup()
            t.setpos(x, y)
            t.pendown()

    t.wait()


if __name__ == "__main__":
    main()
