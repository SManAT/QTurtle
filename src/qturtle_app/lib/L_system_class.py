# -*- coding: utf-8 -*-

"""
A Class, that creates Lindenmayer Strings
"""
from typing import Any


import math


class LSystem:
    angle = 90
    iterations = 2
    axiom = ""
    rules = {}
    code = []
    length = 100

    _legend = {"F": "forward draw", "f": "forward no line", "+": "Winkel°", "-": "-Winkel°", "[": "push", "]": "pop"}

    @classmethod
    def legend(cls) -> str:
        items = list(cls._legend.items())
        erg = ""
        for i in range(0, len(items), 2):
            key1, value1 = items[i]
            line = f"{key1}: {value1:<30}"  # Left-align first column in 30 chars

            # Add second item if exists
            if i + 1 < len(items):
                key2, value2 = items[i + 1]
                line += f"{key2}: {value2}"

            erg += line + "\n"

        return erg

    def __init__(self, angle: int, iterations: int, axiom: str, rules):
        self.angle = angle
        self.iterations = iterations
        self.axiom = axiom
        self.rules = rules

    def output(self, msg):
        print(msg)

    """ Build L-String with rules """

    def getFinalString(self):
        code = self.axiom
        self.output(code)

        if self.iterations > 0:
            for i in range(self.iterations):
                new_code = ""
                for c in code:
                    replaced = False
                    # Regeln durcharbeiten
                    for key, value in self.rules.items():
                        if c == key:
                            new_code += value
                            replaced = True
                            break
                    if replaced == False:
                        # Zeichen übernehmen
                        new_code += c

                code = new_code
                # self.output(code)
        return code
