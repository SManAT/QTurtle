from qturtle_app.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="KreisApprox.svg")
t.speed(0)
t.width(2)

delta_x = 300
x = -300
k = 3
for i in range(3):
    t.teleport(x, 200)
    nPoly(t, k, 100)
    x += delta_x
    k += 2

x = -300
for i in range(2):
    t.teleport(x, -200)
    nPoly(t, k, 100)
    x += delta_x
    k += 10

t.teleport(x, -200)
nPoly(t, 100, 100)

t.save_svg()
