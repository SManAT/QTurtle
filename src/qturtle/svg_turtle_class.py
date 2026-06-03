"""
SVG_Turtle_Output:
Simple wrapper for generating SVG output using turtle-like commands.
SVGTurtle:
Wrapper that uses python turtle for animation and SVG_Turtle for export.

Example:
from qturtle.svg_turtle_class import SVGTurtle

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

"""

import math
import os
from turtle import Turtle

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
        print(f"✓ SVG Turtle created - will save to: {self.filename}")

    def __del__(self):
        """Auto-save SVG when object is destroyed"""
        try:
            self.svg.save_as(self.filename)
        except:
            pass

    def save_svg(self):
        """Save SVG file and display in cell"""
        self.svg.save_as(self.filename)
        print(f"💾 SVG saved to: {self.filename}")

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
        pass

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

    def __init__(self, width=400, height=400, filename="output.svg", bgcolor="lightblue"):
        self.width = width
        self.height = height
        self.filename = filename
        self.turtle = Turtle()

        # Set up SVG_Turtle for export first (creates svg directory and sets final path)
        self.svg_turtle = SVG_Turtle_Output({"filename": filename, "size": (width, height)})

        # Reset turtle to original origin and state
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
        if speed is not None and self.turtle:
            self.turtle.speed(speed)

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

    def shape(self, name):
        if self.turtle:
            self.turtle.shape(name)

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
