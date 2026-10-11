# QTurtle Turtle API

Gültig für `turtle.Turtle` (Python-Standardbibliothek) und `qturtle_app.svg_turtle_class.SVGTurtle`.
Positionen sind Koordinatenpaare `(x, y)`, Winkel in Grad (Standard: 360), `0°` zeigt nach Osten.

## Addons: eigene Befehle

Eigene Python-Dateien (`.py`) im Ordner `addons/` (in der ausführbaren Version neben `QTurtle.exe`) werden beim Start jedes Skripts automatisch geladen. Alle dort definierten Funktionen, Klassen und Variablen ohne führenden Unterstrich (`_`) sind im Skript direkt verfügbar – ganz ohne `import`:

```python
import turtle

t = turtle.Turtle()
stern(t, 100)        # Funktion aus addons/beispiel_addon.py
turtle.done()
```

Regeln:

- Der Dateiname wird zum Modulnamen (`beispiel_addon.py` → Modul `beispiel_addon`, auch per `import beispiel_addon` erreichbar).
- Namen mit führendem Unterstrich (`_privat`) werden nicht exportiert; Dateien, die mit `_` beginnen, werden übersprungen.
- Ein Fehler in einer Addon-Datei bricht das Skript nicht ab – es erscheint nur eine Warnung in der Konsole.
- Definitionen im Skript selbst überschreiben gleichnamige Addon-Funktionen.
- Tippfehler-Hinweise ("Meintest du ...?") schlagen auch Addon-Funktionen vor.

## Punkte und Vektoren (Addon `punkte_vektoren`)

Das Addon `addons/punkte_vektoren.py` stellt Punkte und Vektoren als Zahlenpaare bereit. Intern wird numpy verwendet – im Skript ist davon aber nichts zu sehen, es genügen die Befehle aus dieser Tabelle. Punkte und Vektoren unterstützen `+`, `-`, `*` (mit Zahl) und den Zugriff über `P[0]` (x) und `P[1]` (y) direkt:

```python
P1 = Punkt(0, 0)
P2 = Punkt(0, 400)
P3 = Punkt(400, 0)

r12 = P2 - P1                 # Richtungsvektor von P1 nach P2
print(P1[0], P1[1])           # x- und y-Koordinate
```

| Befehl | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `Punkt` | `Punkt(x, y)` | Erstellt einen Punkt mit den Koordinaten `(x, y)`. | Punkt |
| `Vektor` | `Vektor(x, y)` | Erstellt einen Vektor mit den Komponenten `(x, y)`. | Vektor |
| `richtungsvektor` | `richtungsvektor(P1, P2)` | Berechnet den Vektor von `P1` nach `P2` (entspricht `P2 - P1`). | Vektor |
| `vektor_add` | `vektor_add(v1, v2)` | Addiert zwei Vektoren (verschiebt auch einen Punkt um einen Vektor). | Vektor |
| `vektor_sub` | `vektor_sub(v1, v2)` | Subtrahiert `v2` von `v1`. | Vektor |
| `vektor_mal` | `vektor_mal(v, k)` | Multipliziert einen Vektor mit einer Zahl `k` (verlängert/verkürzt). | Vektor |
| `skalarprodukt` | `skalarprodukt(v1, v2)` | Berechnet das Skalarprodukt zweier Vektoren. | Zahl |
| `kreuzprodukt` | `kreuzprodukt(v1, v2)` | Berechnet das 2D-Kreuzprodukt: `0` = parallel (Punkte auf einer Geraden), `> 0` = `v2` links von `v1`, `< 0` = rechts. | Zahl |
| `laenge` | `laenge(v)` | Berechnet die Länge (den Betrag) eines Vektors. | Zahl |
| `abstand` | `abstand(P1, P2)` | Berechnet den Abstand zwischen zwei Punkten. | Zahl |
| `einheitsvektor` | `einheitsvektor(v)` | Berechnet den Vektor der Länge 1 mit gleicher Richtung (Fehler beim Nullvektor). | Vektor |
| `normalenvektor` | `normalenvektor(v)` | Berechnet den Vektor, der senkrecht auf `v` steht (90°-Drehung). | Vektor |
| `winkel` | `winkel(v1, v2)` | Berechnet den Winkel zwischen zwei Vektoren in Grad (0–180). | Zahl |
| `mittelpunkt` | `mittelpunkt(P1, P2)` | Berechnet den Mittelpunkt der Strecke zwischen zwei Punkten. | Punkt |

## Bewegung

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `forward` / `fd` | `forward(distance)` | Bewegt die Turtle um `distance` in Blickrichtung vorwärts. | – |
| `backward` / `bk` / `back` | `backward(distance)` | Bewegt die Turtle um `distance` rückwärts, ohne die Richtung zu ändern. | – |
| `right` / `rt` | `right(angle)` | Dreht die Turtle um `angle` nach rechts (im Uhrzeigersinn). | – |
| `left` / `lt` | `left(angle)` | Dreht die Turtle um `angle` nach links (gegen den Uhrzeigersinn). | – |
| `goto` / `setpos` / `setposition` | `goto(x, y=None)` – akzeptiert auch `(x, y)`-Tupel | Bewegt die Turtle direkt zur angegebenen Position. | – |
| `setx` | `setx(x)` | Setzt die x-Koordinate, y bleibt gleich. | – |
| `sety` | `sety(y)` | Setzt die y-Koordinate, x bleibt gleich. | – |
| `teleport` | `teleport(x, y=None, *, fill_gap=False)` | Springt zur Position, ohne eine Linie zu zeichnen. | – |
| `home` | `home()` | Bewegt die Turtle zum Ursprung `(0, 0)` und richtet sie nach Osten aus. | – |
| `circle` | `circle(radius, extent=None, steps=None)` | Zeichnet einen Kreis bzw. Kreisbogen (`extent` in Grad) oder ein Vieleck (`steps`). | – |
| `dot` | `dot(size=None, *color)` | Zeichnet einen gefüllten Punkt mit Durchmesser `size` an der aktuellen Position. | – |
| `stamp` | `stamp()` | Stempelt die Turtle-Form an der aktuellen Position auf die Zeichenfläche. | stamp_id |
| `clearstamp` | `clearstamp(stampid)` | Entfernt den Stempel mit der angegebenen ID. | – |
| `clearstamps` | `clearstamps(n=None)` | Entfernt alle (`None`), die ersten `n` oder die letzten `-n` Stempel. | – |
| `undo` | `undo()` | Macht die letzte Turtle-Aktion rückgängig. | – |

## Zustand abfragen

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `pos` / `position` | `pos()` | Liefert die aktuelle Position. | `(x, y)` |
| `xcor` | `xcor()` | Liefert die aktuelle x-Koordinate. | `x` |
| `ycor` | `ycor()` | Liefert die aktuelle y-Koordinate. | `y` |
| `heading` | `heading()` | Liefert die aktuelle Blickrichtung. | Winkel in Grad |
| `distance` | `distance(x, y=None)` | Berechnet den Abstand zu einem Punkt oder einer anderen Turtle. | Distanz |
| `towards` | `towards(x, y=None)` | Berechnet den Winkel von der Turtle zum Zielpunkt. | Winkel zum Ziel |
| `isdown` | `isdown()` | Prüft, ob der Stift unten ist (zeichnet). | `bool` |
| `isvisible` | `isvisible()` | Prüft, ob die Turtle sichtbar ist. | `bool` |
| `filling` | `filling()` | Prüft, ob gerade eine Füllung aktiv ist (`begin_fill` ohne `end_fill`). | `bool` |
| `speed` | `speed(speed=None)` | Setzt oder liefert die Zeichengeschwindigkeit (0 = am schnellsten, 1–10 = langsam bis schnell). | aktuelle Geschwindigkeit |
| `pen` | `pen(pen=None, **pendict)` | Setzt oder liefert alle Stifteigenschaften auf einmal als Dictionary. | Pen-Dict |
| `undobufferentries` | `undobufferentries()` | Liefert die Anzahl der rückgängig machbaren Aktionen. | `int` |

## Stift

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `penup` / `pu` / `up` | `penup()` | Hebt den Stift an – Bewegungen zeichnen nicht mehr. | – |
| `pendown` / `pd` / `down` | `pendown()` | Senkt den Stift – Bewegungen zeichnen wieder. | – |
| `pensize` / `width` | `pensize(width=None)` | Setzt oder liefert die Linienbreite. | aktuelle Breite |
| `pencolor` | `pencolor(*args)` – Farbnamen, `(r, g, b)` oder Hexstrings | Setzt oder liefert die Linienfarbe. | aktuelle Farbe |
| `fillcolor` | `fillcolor(*args)` | Setzt oder liefert die Füllfarbe. | aktuelle Füllfarbe |
| `color` | `color(*args)` – setzt Pen- und Füllfarbe | Setzt Linien- und Füllfarbe gemeinsam oder liefert beide. | `(pencolor, fillcolor)` |
| `begin_fill` | `begin_fill()` | Startet eine Füllung – die folgende Form wird gefüllt. | – |
| `end_fill` | `end_fill()` | Beendet die Füllung und füllt die gezeichnete Form. | – |
| `setundobuffer` | `setundobuffer(size)` | Legt fest, wie viele Aktionen rückgängig gemacht werden können (`None` deaktiviert). | – |

## Ausrichtung und Winkel

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `setheading` / `seth` | `setheading(to_angle)` | Richtet die Turtle auf einen absoluten Winkel aus (0 = Osten, 90 = Norden). | – |
| `degrees` | `degrees(fullcircle=360.0)` | Stellt die Winkeleinheit auf Grad um (optional mit eigener Vollkreis-Teilung). | – |
| `radians` | `radians()` | Stellt die Winkeleinheit auf Bogenmaß um. | – |

## Sichtbarkeit und Form

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `showturtle` / `st` | `showturtle()` | Macht die Turtle sichtbar. | – |
| `hideturtle` / `ht` | `hideturtle()` | Versteckt die Turtle (zeichnet weiter, oft schneller). | – |
| `shape` | `shape(name=None)` – `"classic"`, `"turtle"`, `"circle"`, `"square"`, `"triangle"`, `"arrow"` | Setzt oder liefert die Form der Turtle. | aktueller Name |
| `shapesize` / `turtlesize` | `shapesize(stretch_wid=None, stretch_len=None, outline=None)` | Streckt die Turtle-Form in Breite/Länge und setzt die Umrissbreite. | aktuelles Tuple |
| `resizemode` | `resizemode(rmode=None)` – `"auto"`, `"user"`, `"noresize"` | Legt fest, wie sich die Turtle-Form an die Stiftbreite anpasst. | aktueller Modus |
| `shearfactor` | `shearfactor(shear=None)` | Setzt oder liefert die Scherung der Turtle-Form. | aktueller Faktor |
| `shapetransform` | `shapetransform(t11=None, t12=None, t21=None, t22=None)` | Setzt oder liefert die Transformationsmatrix der Turtle-Form. | Transformationsmatrix |
| `tilt` | `tilt(angle)` | Dreht nur die Form um `angle`, nicht die Bewegungsrichtung. | – |
| `tiltangle` | `tiltangle(angle=None)` | Setzt oder liefert den Neigungswinkel der Form. | aktueller Winkel |

## Text und Zeichnung

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `write` | `write(arg, move=False, align="left", font=("Arial", 8, "normal"))` – `align`: `"left"`, `"center"`, `"right"` | Schreibt Text an die aktuelle Position; mit `move=True` wandert die Turtle ans Textende. | – |
| `begin_poly` | `begin_poly()` | Beginnt die Aufzeichnung der Eckpunkte eines Polygons. | – |
| `end_poly` | `end_poly()` | Beendet die Aufzeichnung der Polygon-Eckpunkte. | – |
| `get_poly` | `get_poly()` | Liefert das zuletzt aufgezeichnete Polygon. | Liste von `(x, y)` |
| `reset` | `reset()` | Löscht die Zeichnung der Turtle und setzt sie in den Ausgangszustand zurück. | – |
| `clear` | `clear()` | Löscht die Zeichnung der Turtle, Position und Einstellungen bleiben. | – |

## Sonstiges

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `clone` | `clone()` | Erzeugt eine Kopie der Turtle mit gleicher Position und gleichen Einstellungen. | neue Turtle-Instanz |
| `getturtle` / `getpen` | `getturtle()` | Liefert das Turtle-Objekt selbst. | die Turtle selbst |
| `getscreen` | `getscreen()` | Liefert das Fenster (Screen), auf dem die Turtle zeichnet. | Screen-Objekt |
| `onclick` | `onclick(fun, btn=1, add=None)` | Ruft `fun(x, y)` auf, wenn die Turtle angeklickt wird. | – |
| `onrelease` | `onrelease(fun, btn=1, add=None)` | Ruft `fun(x, y)` auf, wenn die Maustaste über der Turtle losgelassen wird. | – |
| `ondrag` | `ondrag(fun, btn=1, add=None)` | Ruft `fun(x, y)` beim Ziehen der Turtle mit der Maus auf. | – |

## SVGTurtle-Erweiterungen (nur `qturtle_app.svg_turtle_class.SVGTurtle`)

| Methode | Signatur | Beschreibung | Rückgabe |
|---|---|---|---|
| `SVGTurtle` | `SVGTurtle(width=400, height=400, filename="output.svg", bgcolor="white")` | Erzeugt eine Turtle, die gleichzeitig animiert zeichnet und ein SVG aufbaut; `bgcolor` setzt den Hintergrund in beiden, Standard ist Weiß. | – |
| `save_svg` | `save_svg()` | Schreibt die SVG-Datei ins `svg/`-Verzeichnis. | – |
| `createFilledCircle` | `createFilledCircle(x, y, color, radius, winkel=360, steps=50)` | Zeichnet einen gefüllten Kreis bzw. Kreissektor mit Mittelpunkt `(x, y)`. | – |
| `drawArc` | `drawArc(mx, my, radius, startangle, angle, steps=5)` | Zeichnet einen Kreisbogen um `(mx, my)` ab `startangle` über `angle` Grad. | – |
| `getPosviaAngle` | `getPosviaAngle(radius, angle)` | Berechnet den Punkt auf einem Kreis mit `radius` beim Winkel `angle`. | `(int, int)` |
| `toRad` | `toRad(w)` | Rechnet einen Winkel von Grad in Bogenmaß um. | Bogenmaß |
| `drawLSystem` | `drawLSystem(lstr, L, angle, iterations)` | Zeichnet einen L-System-String mit Schrittlänge `L` und Drehwinkel `angle`: `F` vor, `+` links, `-` rechts, `f` vor ohne Zeichnen. | – |

Ereignis-Callbacks (`onclick`, `onrelease`, `ondrag`) wirken bei `SVGTurtle` nur auf das animierte turtle-Fenster; das SVG ist statisch. `shape()` ändert nur die Form im animierten Fenster und hat keinen Effekt auf das SVG.
