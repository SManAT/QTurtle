# QTurtle Turtle API

Gültig für `turtle.Turtle` (Python-Standardbibliothek) und `qturtle_app.svg_turtle_class.SVGTurtle`.
Positionen sind Koordinatenpaare `(x, y)`, Winkel in Grad (Standard: 360), `0°` zeigt nach Osten.

## Bewegung

| Methode | Signatur | Rückgabe |
|---|---|---|
| `forward` / `fd` | `forward(distance)` | – |
| `backward` / `bk` / `back` | `backward(distance)` | – |
| `right` / `rt` | `right(angle)` | – |
| `left` / `lt` | `left(angle)` | – |
| `goto` / `setpos` / `setposition` | `goto(x, y=None)` – akzeptiert auch `(x, y)`-Tupel | – |
| `setx` | `setx(x)` | – |
| `sety` | `sety(y)` | – |
| `teleport` | `teleport(x, y=None, *, fill_gap=False)` | – |
| `home` | `home()` | – |
| `circle` | `circle(radius, extent=None, steps=None)` | – |
| `dot` | `dot(size=None, *color)` | – |
| `stamp` | `stamp()` | stamp_id |
| `clearstamp` | `clearstamp(stampid)` | – |
| `clearstamps` | `clearstamps(n=None)` | – |
| `undo` | `undo()` | – |

## Zustand abfragen

| Methode | Signatur | Rückgabe |
|---|---|---|
| `pos` / `position` | `pos()` | `(x, y)` |
| `xcor` | `xcor()` | `x` |
| `ycor` | `ycor()` | `y` |
| `heading` | `heading()` | Winkel in Grad |
| `distance` | `distance(x, y=None)` | Distanz |
| `towards` | `towards(x, y=None)` | Winkel zum Ziel |
| `isdown` | `isdown()` | `bool` |
| `isvisible` | `isvisible()` | `bool` |
| `filling` | `filling()` | `bool` |
| `speed` | `speed(speed=None)` | aktuelle Geschwindigkeit |
| `pen` | `pen(pen=None, **pendict)` | Pen-Dict |
| `undobufferentries` | `undobufferentries()` | `int` |

## Stift

| Methode | Signatur | Rückgabe |
|---|---|---|
| `penup` / `pu` / `up` | `penup()` | – |
| `pendown` / `pd` / `down` | `pendown()` | – |
| `pensize` / `width` | `pensize(width=None)` | aktuelle Breite |
| `pencolor` | `pencolor(*args)` – Farbnamen, `(r, g, b)` oder Hexstrings | aktuelle Farbe |
| `fillcolor` | `fillcolor(*args)` | aktuelle Füllfarbe |
| `color` | `color(*args)` – setzt Pen- und Füllfarbe | `(pencolor, fillcolor)` |
| `begin_fill` | `begin_fill()` | – |
| `end_fill` | `end_fill()` | – |
| `setundobuffer` | `setundobuffer(size)` | – |

## Ausrichtung und Winkel

| Methode | Signatur | Rückgabe |
|---|---|---|
| `setheading` / `seth` | `setheading(to_angle)` | – |
| `degrees` | `degrees(fullcircle=360.0)` | – |
| `radians` | `radians()` | – |

## Sichtbarkeit und Form

| Methode | Signatur | Rückgabe |
|---|---|---|
| `showturtle` / `st` | `showturtle()` | – |
| `hideturtle` / `ht` | `hideturtle()` | – |
| `shape` | `shape(name=None)` – `"classic"`, `"turtle"`, `"circle"`, `"square"`, `"triangle"`, `"arrow"` | aktueller Name |
| `shapesize` / `turtlesize` | `shapesize(stretch_wid=None, stretch_len=None, outline=None)` | aktuelles Tuple |
| `resizemode` | `resizemode(rmode=None)` – `"auto"`, `"user"`, `"noresize"` | aktueller Modus |
| `shearfactor` | `shearfactor(shear=None)` | aktueller Faktor |
| `shapetransform` | `shapetransform(t11=None, t12=None, t21=None, t22=None)` | Transformationsmatrix |
| `tilt` | `tilt(angle)` | – |
| `tiltangle` | `tiltangle(angle=None)` | aktueller Winkel |

## Text und Zeichnung

| Methode | Signatur | Rückgabe |
|---|---|---|
| `write` | `write(arg, move=False, align="left", font=("Arial", 8, "normal"))` – `align`: `"left"`, `"center"`, `"right"` | – |
| `begin_poly` | `begin_poly()` | – |
| `end_poly` | `end_poly()` | – |
| `get_poly` | `get_poly()` | Liste von `(x, y)` |
| `reset` | `reset()` | – |
| `clear` | `clear()` | – |

## Sonstiges

| Methode | Signatur | Rückgabe |
|---|---|---|
| `clone` | `clone()` | neue Turtle-Instanz |
| `getturtle` / `getpen` | `getturtle()` | die Turtle selbst |
| `getscreen` | `getscreen()` | Screen-Objekt |
| `onclick` | `onclick(fun, btn=1, add=None)` | – |
| `onrelease` | `onrelease(fun, btn=1, add=None)` | – |
| `ondrag` | `ondrag(fun, btn=1, add=None)` | – |

## SVGTurtle-Erweiterungen (nur `qturtle_app.svg_turtle_class.SVGTurtle`)

| Methode | Signatur | Rückgabe |
|---|---|---|
| `SVGTurtle` | `SVGTurtle(width=400, height=400, filename="output.svg", bgcolor="white")` – `bgcolor` setzt den Hintergrund im SVG und im animierten Fenster, Standard ist Weiß | – |
| `save_svg` | `save_svg()` – schreibt die SVG-Datei ins `svg/`-Verzeichnis | – |
| `createFilledCircle` | `createFilledCircle(x, y, color, radius, winkel=360, steps=50)` | – |
| `drawArc` | `drawArc(mx, my, radius, startangle, angle, steps=5)` | – |
| `getPosviaAngle` | `getPosviaAngle(radius, angle)` | `(int, int)` |
| `toRad` | `toRad(w)` | Bogenmaß |
| `drawLSystem` | `drawLSystem(lstr, L, angle, iterations)` – `F` vor, `+` links, `-` rechts, `f` vor ohne Zeichnen | – |

Ereignis-Callbacks (`onclick`, `onrelease`, `ondrag`) wirken bei `SVGTurtle` nur auf das animierte turtle-Fenster; das SVG ist statisch. `shape()` ändert nur die Form im animierten Fenster und hat keinen Effekt auf das SVG.
