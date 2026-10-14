from qturtle_app.svg_turtle_class import SVGTurtle
import math

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="01_square.svg")
t.speed(3)


def liniertesDreieck(abstand):
    h = t.heading()

    for i in range(8):
        t.setheading(h)
       
        print(t.heading())
        t.teleport(0, abstand * i)
        t.right(45)
        t.forward(math.sqrt(2) * abstand * i)


abstand = 30
liniertesDreieck(abstand)
t.left(180)
liniertesDreieck(abstand)


t.save_svg()
