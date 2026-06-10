from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="01_square.svg", bgcolor="lightblue")
t.shape("turtle")
t.color("green")
t.speed(3)

# Quadrat zeichnen
for i in range(4):
    t.forward(100)
    t.right(90)

t.save_svg()
