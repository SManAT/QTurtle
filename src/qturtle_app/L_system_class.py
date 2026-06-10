# -*- coding: utf-8 -*-

"""
A Class, that creates Lindenmayer Strings
"""
import math


class LSystem:
    angle = 90
    iterations = 2
    axiom = ""
    rules = {}
    code = []
    length = 100

    alphabet = {"+": "Winkel°", "-": "-Winkel°", "[": "push", "]": "pop", "F": "forward"}

    def __init__(self, angle: int, iterations: int, length: int, axiom: str, rules):
        self.angle = angle
        self.iterations = iterations
        self.length = length
        self.axiom = axiom
        self.rules = rules

        # get Final String

    def output(self, msg):
        print(msg)

    def getFinalString(self, code):
        erg = ""
        """
    for char in code:
      if self.is_Alphabet(char)==False:
        erg += char
    """
        return erg

    """ checks if an character is from alphabet """

    def is_Alphabet(self, char):
        found = False
        for aChar in self.alphabet:
            if aChar == char:
                found = True
        return found

    """ Die Iterationen werden durchgeführt """
    """
  def iterate(self, iterationen):
    code = self.axiom
    if iterationen>0:
      for i in range(iterationen):
        new_code = ""
        for c in code:
          #Regeln durcharbeiten
          replaced=False
          for k in range(len(self.regeln)):
            item = self.regeln[k]
            if c==item[0]:
              new_code += item[1]
              replaced=True
          if replaced==False:
            #Zeichen übernehmen
            new_code += c

        code = new_code
        self.output(code)

    print "Fertiger Code: %s" % (self.getFinalCode(code))
    self.code = code
    st()
    """

    """ zeichnet das L System """
    """
  def draw(self, Tool):
    for char in self.code:
    if char=="F":
      forward(self.length)
      Tool.SVG_DrawTo(getX(), getY())
      #self.output("F: %s" % self.length)

    elif char=="+":
      left(self.alpha)
      #self.output("+: %s" % self.alpha)

    elif char=="-":
      right(self.alpha)
      #self.output("-: %s" % self.alpha)

    elif char=="f":
      pu()
      forward(self.length)
      pd()
      Tool.SVG_MoveTo(getX(), getY())
      #self.output("f: %s" % self.length)
    else:
      #check if constant or alphabet
      if self.is_Alphabet(char):
        #ist im Alphabet > mach nichts
        pass
      else:
        #wird wie F behandelt
        forward(self.length)
        Tool.SVG_DrawTo(getX(), getY())
    """
