"""
SVG_Turtle_Output:
Simple wrapper for generating SVG output using turtle-like commands.
SVGTurtle:
Wrapper that uses python turtle for animation and SVG_Turtle for export.

Example:
from qturtle.svg_turtle_class import SVGTurtle

# Turtle erstellen und konfigurieren
t = SVGTurtle(width=400, height=400, filename="01_square.svg")
t.color("green")
t.speed(3)

# Quadrat zeichnen
for i in range(4):
    t.forward(100)
    t.right(90)

t.save_svg()

"""

import math
import os

try:
    from turtle import Turtle as _BaseTurtle

    _TURTLE_AVAILABLE = True
except Exception as _turtle_import_error:
    _BaseTurtle = None  # type: ignore[assignment,misc]
    _TURTLE_AVAILABLE = False
    import sys as _sys

    print(f"Warning: turtle animation unavailable ({_turtle_import_error})", file=_sys.stderr)

from svg_turtle import SvgTurtle


class SVG_Turtle_Output:
    def __init__(self, params=None, width=500, height=500):
        if params is None:
            params = {}

        filename = params.get("filename", "output.svg")
        svg_dir = "svg"
        os.makedirs(svg_dir, exist_ok=True)
        self.filename = os.path.join(svg_dir, filename)
        self.size = params.get("size", (width, height))
        width, height = self.size

        self.svg = SvgTurtle(width, height)

        bgcolor = params.get("bgcolor")
        if bgcolor is None:
            bgcolor = "white"
        self.svg.getscreen().bgcolor(bgcolor)

    def __del__(self):
        """Auto-save SVG when object is destroyed"""
        try:
            self.svg.save_as(self.filename)
        except:
            pass

    def save_svg(self):
        """Save SVG file and display in cell"""
        self.svg.save_as(self.filename)
        print(f"SVG saved to: {self.filename}")

    def penup(self):
        self.svg.penup()

    def pendown(self):
        self.svg.pendown()

    def forward(self, distance):
        self.svg.forward(distance)

    def backward(self, distance):
        self.svg.backward(distance)

    def right(self, angle):
        self.svg.right(angle)

    def left(self, angle):
        self.svg.left(angle)

    def goto(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        self.svg.goto(x, y)

    def setheading(self, to_angle):
        self.svg.setheading(to_angle)

    def home(self):
        self.svg.home()

    def circle(self, radius, angle=None, steps=None):
        if angle is None and steps is None:
            self.svg.circle(radius)
        elif steps is None:
            self.svg.circle(radius, angle)
        else:
            self.svg.circle(radius, angle, steps)

    def fillcolor(self, *args):
        self.svg.fillcolor(*args)

    def pencolor(self, *args):
        self.svg.pencolor(*args)

    def begin_fill(self):
        self.svg.begin_fill()

    def end_fill(self):
        self.svg.end_fill()

    def speed(self, speed=None):
        return self.svg.speed(speed)

    def dot(self, size=None, *color):
        if size is None:
            self.svg.dot()
        else:
            self.svg.dot(size, *color)

    def write(self, arg, move=False, align="left", font=("Arial", 8, "normal")):
        self.svg.write(arg, move, align, font)

    def pensize(self, width=None):
        if width is None:
            try:
                return self.svg.pensize()
            except AttributeError:
                return 1
        else:
            try:
                self.svg.pensize(width)
            except AttributeError:
                pass

    def width(self, width=None):
        if width is None:
            try:
                return self.svg.width()
            except AttributeError:
                return 1
        else:
            try:
                self.svg.width(width)
            except AttributeError:
                pass

    # ------------------------------------------------------------------
    # Original turtle-API: Aliase
    # ------------------------------------------------------------------
    def fd(self, distance):
        self.svg.fd(distance)

    def bk(self, distance):
        self.svg.bk(distance)

    def back(self, distance):
        self.svg.back(distance)

    def rt(self, angle):
        self.svg.rt(angle)

    def lt(self, angle):
        self.svg.lt(angle)

    def pu(self):
        self.svg.pu()

    def up(self):
        self.svg.up()

    def pd(self):
        self.svg.pd()

    def down(self):
        self.svg.down()

    def seth(self, to_angle):
        self.svg.seth(to_angle)

    def setpos(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        self.svg.setpos(x, y)

    def setposition(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        self.svg.setposition(x, y)

    def teleport(self, x, y=None, *, fill_gap=False):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        self.svg.teleport(x, y, fill_gap=fill_gap)

    # ------------------------------------------------------------------
    # Original turtle-API: Positions- und Statusabfragen
    # ------------------------------------------------------------------
    def pos(self):
        return self.svg.pos()

    def position(self):
        return self.svg.position()

    def xcor(self):
        return self.svg.xcor()

    def ycor(self):
        return self.svg.ycor()

    def heading(self):
        return self.svg.heading()

    def distance(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        return self.svg.distance(x, y)

    def towards(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        return self.svg.towards(x, y)

    def isdown(self):
        return self.svg.isdown()

    def isvisible(self):
        return self.svg.isvisible()

    def filling(self):
        return self.svg.filling()

    def setx(self, x):
        self.svg.setx(x)

    def sety(self, y):
        self.svg.sety(y)

    def degrees(self, fullcircle=360.0):
        self.svg.degrees(fullcircle)

    def radians(self):
        self.svg.radians()

    def pen(self, pen=None, **pendict):
        return self.svg.pen(pen, **pendict)

    # ------------------------------------------------------------------
    # Original turtle-API: Sichtbarkeit und Form
    # ------------------------------------------------------------------
    def shape(self, name=None):
        return self.svg.shape(name)

    def hideturtle(self):
        self.svg.hideturtle()

    def ht(self):
        self.svg.ht()

    def showturtle(self):
        self.svg.showturtle()

    def st(self):
        self.svg.st()

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        return self.svg.shapesize(stretch_wid, stretch_len, outline)

    def turtlesize(self, stretch_wid=None, stretch_len=None, outline=None):
        return self.svg.turtlesize(stretch_wid, stretch_len, outline)

    def resizemode(self, rmode=None):
        return self.svg.resizemode(rmode)

    def shearfactor(self, shear=None):
        return self.svg.shearfactor(shear)

    def shapetransform(self, t11=None, t12=None, t21=None, t22=None):
        return self.svg.shapetransform(t11, t12, t21, t22)

    def tilt(self, angle):
        self.svg.tilt(angle)

    def tiltangle(self, angle=None):
        return self.svg.tiltangle(angle)

    # ------------------------------------------------------------------
    # Original turtle-API: Reset, Undo und Stempel
    # ------------------------------------------------------------------
    def reset(self):
        self.svg.reset()

    def clear(self):
        self.svg.clear()

    def undo(self):
        self.svg.undo()

    def setundobuffer(self, size):
        self.svg.setundobuffer(size)

    def undobufferentries(self):
        return self.svg.undobufferentries()

    def stamp(self):
        return self.svg.stamp()

    def clearstamp(self, stampid):
        self.svg.clearstamp(stampid)

    def clearstamps(self, n=None):
        self.svg.clearstamps(n)

    # ------------------------------------------------------------------
    # Original turtle-API: Polygone
    # ------------------------------------------------------------------
    def begin_poly(self):
        self.svg.begin_poly()

    def end_poly(self):
        self.svg.end_poly()

    def get_poly(self):
        return self.svg.get_poly()

    # ------------------------------------------------------------------
    # Original turtle-API: Sonstiges
    # ------------------------------------------------------------------
    def clone(self):
        return self.svg.clone()

    def getpen(self):
        return self.svg.getpen()

    def getscreen(self):
        return self.svg.getscreen()

    def getturtle(self):
        return self.svg.getturtle()

    # Your extended methods
    def toRad(self, w):
        return w * math.pi / 180

    def createFilledCircle(self, x, y, color, radius, winkel=360, steps=50):
        """Create a filled circle centered at (x, y)"""
        self.penup()
        self.goto(x, y - radius)
        self.pendown()

        self.fillcolor(color)
        self.begin_fill()
        self.circle(radius, winkel, steps)
        self.end_fill()

    def getPosviaAngle(self, radius, angle):
        x = radius * math.cos(self.toRad(angle))
        y = radius * math.sin(self.toRad(angle))
        return int(x), int(y)

    def getTangente(self, radius, x):
        """Tangenten winkel am Kreis an der Stelle x berechnen"""
        winkel = 0
        try:
            k = -(x / math.sqrt(radius**2 - x**2))
            print(f"Tangent slope: {k}")
        except Exception:
            winkel = 90
        return winkel

    def drawArc(self, mx, my, radius, startangle, angle, steps=5):
        if angle < 0:
            steps *= -1
        self.penup()
        x, y = self.getPosviaAngle(radius, startangle)
        self.goto(mx + x, my + y)
        self.pendown()
        for i in range(startangle, startangle + angle + steps, steps):
            x, y = self.getPosviaAngle(radius, i)
            self.goto(mx + x, my + y)


class SVGTurtle:
    """
    Wrapper that combines turtle animation with SVG export.
    Use like a regular turtle, but get both animated display and SVG output.
    """

    def __init__(self, width=400, height=400, filename="output.svg", bgcolor="white"):
        self.filename = filename
        try:
            self.turtle = _BaseTurtle() if _TURTLE_AVAILABLE else None
        except Exception as e:
            import sys as _sys

            print(f"Warning: could not create turtle window ({e})", file=_sys.stderr)
            self.turtle = None

        # Set up SVG_Turtle for export first (creates svg directory and sets final path)
        self.svg_turtle = SVG_Turtle_Output({"filename": filename, "size": (width, height), "bgcolor": bgcolor})

        # Reset turtle to original origin and state
        if bgcolor and self.turtle:
            self.turtle.getscreen().bgcolor(bgcolor)

        self.home()
        self.pendown()

    def forward(self, distance):
        if self.turtle:
            self.turtle.forward(distance)
        self.svg_turtle.forward(distance)

    def backward(self, distance):
        if self.turtle:
            self.turtle.backward(distance)
        self.svg_turtle.backward(distance)

    def right(self, angle):
        if self.turtle:
            self.turtle.right(angle)
        self.svg_turtle.right(angle)

    def left(self, angle):
        if self.turtle:
            self.turtle.left(angle)
        self.svg_turtle.left(angle)

    def penup(self):
        if self.turtle:
            self.turtle.penup()
        self.svg_turtle.penup()

    def pendown(self):
        if self.turtle:
            self.turtle.pendown()
        self.svg_turtle.pendown()

    def goto(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        if self.turtle:
            self.turtle.goto(x, y)
        self.svg_turtle.goto(x, y)

    def setheading(self, angle):
        if self.turtle:
            self.turtle.setheading(angle)
        self.svg_turtle.setheading(angle)

    def home(self):
        if self.turtle:
            self.turtle.home()
        self.svg_turtle.home()

    def circle(self, radius, angle=None, steps=None):
        if self.turtle:
            if angle is None and steps is None:
                self.turtle.circle(radius)
            elif steps is None:
                self.turtle.circle(radius, angle)
            else:
                self.turtle.circle(radius, angle, steps)

        if angle is None and steps is None:
            self.svg_turtle.circle(radius)
        elif steps is None:
            self.svg_turtle.circle(radius, angle)
        else:
            self.svg_turtle.circle(radius, angle, steps)

    def color(self, *args):
        if self.turtle:
            self.turtle.color(*args)
        # For SVG, use pencolor
        self.svg_turtle.pencolor(*args)

    def pencolor(self, *args):
        if self.turtle:
            self.turtle.pencolor(*args)
        self.svg_turtle.pencolor(*args)

    def fillcolor(self, *args):
        if self.turtle:
            self.turtle.fillcolor(*args)
        self.svg_turtle.fillcolor(*args)

    def begin_fill(self):
        if self.turtle:
            self.turtle.begin_fill()
        self.svg_turtle.begin_fill()

    def end_fill(self):
        if self.turtle:
            self.turtle.end_fill()
        self.svg_turtle.end_fill()

    def speed(self, speed=None):
        if self.turtle:
            return self.turtle.speed(speed)
        return self.svg_turtle.speed(speed)

    def dot(self, size=None, *color):
        if self.turtle:
            if size is None:
                self.turtle.dot()
            else:
                self.turtle.dot(size, *color)

        if size is None:
            self.svg_turtle.dot()
        else:
            self.svg_turtle.dot(size, *color)

    def write(self, text, move=False, align="left", font=("Arial", 8, "normal")):
        if self.turtle:
            self.turtle.write(text, move, align, font)
        self.svg_turtle.write(text, move, align, font)

    def shape(self, name=None):
        if self.turtle:
            self.turtle.shape(name)
        return self.svg_turtle.shape(name)

    def pensize(self, width=None):
        if width is None:
            return self.svg_turtle.pensize()
        else:
            if self.turtle:
                try:
                    self.turtle.pensize(width)
                except AttributeError:
                    pass
            self.svg_turtle.pensize(width)

    def width(self, width=None):
        if width is None:
            return self.svg_turtle.width()
        else:
            if self.turtle:
                try:
                    self.turtle.width(width)
                except AttributeError:
                    pass
            self.svg_turtle.width(width)

    # ------------------------------------------------------------------
    # Original turtle-API: Aliase
    # ------------------------------------------------------------------
    def fd(self, distance):
        self.forward(distance)

    def bk(self, distance):
        self.backward(distance)

    def back(self, distance):
        self.backward(distance)

    def rt(self, angle):
        self.right(angle)

    def lt(self, angle):
        self.left(angle)

    def pu(self):
        self.penup()

    def up(self):
        self.penup()

    def pd(self):
        self.pendown()

    def down(self):
        self.pendown()

    def seth(self, to_angle):
        self.setheading(to_angle)

    def setpos(self, x, y=None):
        self.goto(x, y)

    def setposition(self, x, y=None):
        self.goto(x, y)

    def teleport(self, x, y=None, *, fill_gap=False):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        if self.turtle:
            self.turtle.teleport(x, y, fill_gap=fill_gap)
        self.svg_turtle.teleport(x, y, fill_gap=fill_gap)

    # ------------------------------------------------------------------
    # Original turtle-API: Positions- und Statusabfragen
    # ------------------------------------------------------------------
    def pos(self):
        if self.turtle:
            return self.turtle.pos()
        return self.svg_turtle.pos()

    def position(self):
        return self.pos()

    def xcor(self):
        if self.turtle:
            return self.turtle.xcor()
        return self.svg_turtle.xcor()

    def ycor(self):
        if self.turtle:
            return self.turtle.ycor()
        return self.svg_turtle.ycor()

    def heading(self):
        if self.turtle:
            return self.turtle.heading()
        return self.svg_turtle.heading()

    def distance(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        if self.turtle:
            return self.turtle.distance(x, y)
        return self.svg_turtle.distance(x, y)

    def towards(self, x, y=None):
        if y is None and hasattr(x, "__iter__"):
            x, y = x
        if self.turtle:
            return self.turtle.towards(x, y)
        return self.svg_turtle.towards(x, y)

    def isdown(self):
        if self.turtle:
            return self.turtle.isdown()
        return self.svg_turtle.isdown()

    def isvisible(self):
        if self.turtle:
            return self.turtle.isvisible()
        return self.svg_turtle.isvisible()

    def filling(self):
        if self.turtle:
            return self.turtle.filling()
        return self.svg_turtle.filling()

    def setx(self, x):
        if self.turtle:
            self.turtle.setx(x)
        self.svg_turtle.setx(x)

    def sety(self, y):
        if self.turtle:
            self.turtle.sety(y)
        self.svg_turtle.sety(y)

    def degrees(self, fullcircle=360.0):
        if self.turtle:
            self.turtle.degrees(fullcircle)
        self.svg_turtle.degrees(fullcircle)

    def radians(self):
        if self.turtle:
            self.turtle.radians()
        self.svg_turtle.radians()

    def pen(self, pen=None, **pendict):
        if self.turtle:
            self.turtle.pen(pen, **pendict)
        return self.svg_turtle.pen(pen, **pendict)

    # ------------------------------------------------------------------
    # Original turtle-API: Sichtbarkeit und Form
    # ------------------------------------------------------------------
    def hideturtle(self):
        if self.turtle:
            self.turtle.hideturtle()
        self.svg_turtle.hideturtle()

    def ht(self):
        self.hideturtle()

    def showturtle(self):
        if self.turtle:
            self.turtle.showturtle()
        self.svg_turtle.showturtle()

    def st(self):
        self.showturtle()

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        if self.turtle:
            self.turtle.shapesize(stretch_wid, stretch_len, outline)
        return self.svg_turtle.shapesize(stretch_wid, stretch_len, outline)

    def turtlesize(self, stretch_wid=None, stretch_len=None, outline=None):
        return self.shapesize(stretch_wid, stretch_len, outline)

    def resizemode(self, rmode=None):
        if self.turtle:
            self.turtle.resizemode(rmode)
        return self.svg_turtle.resizemode(rmode)

    def shearfactor(self, shear=None):
        if self.turtle:
            self.turtle.shearfactor(shear)
        return self.svg_turtle.shearfactor(shear)

    def shapetransform(self, t11=None, t12=None, t21=None, t22=None):
        if self.turtle:
            self.turtle.shapetransform(t11, t12, t21, t22)
        return self.svg_turtle.shapetransform(t11, t12, t21, t22)

    def tilt(self, angle):
        if self.turtle:
            self.turtle.tilt(angle)
        self.svg_turtle.tilt(angle)

    def tiltangle(self, angle=None):
        if self.turtle:
            return self.turtle.tiltangle(angle)
        return self.svg_turtle.tiltangle(angle)

    # ------------------------------------------------------------------
    # Original turtle-API: Reset, Undo und Stempel
    # ------------------------------------------------------------------
    def reset(self):
        if self.turtle:
            self.turtle.reset()
        self.svg_turtle.reset()

    def clear(self):
        if self.turtle:
            self.turtle.clear()
        self.svg_turtle.clear()

    def undo(self):
        if self.turtle:
            self.turtle.undo()
        self.svg_turtle.undo()

    def setundobuffer(self, size):
        if self.turtle:
            self.turtle.setundobuffer(size)
        self.svg_turtle.setundobuffer(size)

    def undobufferentries(self):
        if self.turtle:
            return self.turtle.undobufferentries()
        return self.svg_turtle.undobufferentries()

    def stamp(self):
        if self.turtle:
            self.turtle.stamp()
        return self.svg_turtle.stamp()

    def clearstamp(self, stampid):
        if self.turtle:
            self.turtle.clearstamp(stampid)
        self.svg_turtle.clearstamp(stampid)

    def clearstamps(self, n=None):
        if self.turtle:
            self.turtle.clearstamps(n)
        self.svg_turtle.clearstamps(n)

    # ------------------------------------------------------------------
    # Original turtle-API: Polygone
    # ------------------------------------------------------------------
    def begin_poly(self):
        if self.turtle:
            self.turtle.begin_poly()
        self.svg_turtle.begin_poly()

    def end_poly(self):
        if self.turtle:
            self.turtle.end_poly()
        self.svg_turtle.end_poly()

    def get_poly(self):
        if self.turtle:
            return self.turtle.get_poly()
        return self.svg_turtle.get_poly()

    # ------------------------------------------------------------------
    # Original turtle-API: Sonstiges
    # ------------------------------------------------------------------
    def clone(self):
        if self.turtle:
            self.turtle.clone()
        return self.svg_turtle.clone()

    def getpen(self):
        if self.turtle:
            return self.turtle.getpen()
        return self.svg_turtle.getpen()

    def getscreen(self):
        if self.turtle:
            return self.turtle.getscreen()
        return self.svg_turtle.getscreen()

    def getturtle(self):
        return self

    # ------------------------------------------------------------------
    # Ereignisse (nur fuer die animierte turtle, SVG ist statisch)
    # ------------------------------------------------------------------
    def onclick(self, fun, btn=1, add=None):
        if self.turtle:
            self.turtle.onclick(fun, btn, add)

    def onrelease(self, fun, btn=1, add=None):
        if self.turtle:
            self.turtle.onrelease(fun, btn, add)

    def ondrag(self, fun, btn=1, add=None):
        if self.turtle:
            self.turtle.ondrag(fun, btn, add)

    def save_svg(self):
        """Save the SVG file and display in current cell"""
        self.svg_turtle.save_svg()

    def createFilledCircle(self, x, y, color, radius, winkel=360, steps=50):
        """Create a filled circle centered at (x, y)"""
        self.svg_turtle.createFilledCircle(x, y, color, radius, winkel, steps)

    def drawArc(self, mx, my, radius, startangle, angle, steps=5):
        """Draw an arc"""
        self.svg_turtle.drawArc(mx, my, radius, startangle, angle, steps)

    def getPosviaAngle(self, radius, angle):
        """Get position via angle"""
        return self.svg_turtle.getPosviaAngle(radius, angle)

    def drawLSystem(self, lstr: str, L, angle, iterations):
        """Draw a Lindenmayer String"""
        L = L // iterations
        for char in lstr:
            if char == "F":
                self.forward(L)
            elif char == "+":
                self.left(angle)
            elif char == "-":
                self.right(angle)
            elif char == "f":
                self.penup()
                self.forward(L)
                self.pendown()
