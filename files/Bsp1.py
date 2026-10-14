from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="Bsp1.svg")
t.speed(3)

abstand = 20
for i in range(10):
    t.teleport(0, abstand * i)
    t.goto(abstand * i, 0)

t.save_svg()
