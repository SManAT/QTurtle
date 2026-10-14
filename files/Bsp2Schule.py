from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="01_square.svg")
t.speed(3)

P1 = Punkt(0, 0)
P2 = Punkt(0, 200)
P3 = Punkt(200, 0)

# Punkte verbinden
t.teleport(P1)
t.goto(P2)
t.teleport(P1)
t.goto(P3)

# Richtungsvektor
v12 = P2 - P1

Q = v12 / 4 + P1

print(Q)


t.save_svg()
