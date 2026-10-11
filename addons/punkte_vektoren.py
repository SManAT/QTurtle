# Punkte und Vektoren für QTurtle
#
# Dieses Addon stellt Punkte und Vektoren als numpy-Arrays bereit.
# Schülerinnen und Schüler arbeiten NICHT direkt mit numpy – sie verwenden
# nur die Befehle aus dieser Datei (z.B. Punkt, Vektor, abstand, ...).
#
# Punkte und Vektoren verhalten sich wie Zahlenpaare:
#     P1 = Punkt(0, 0)
#     P2 = Punkt(0, 400)
#     r = P2 - P1        # Richtungsvektor von P1 nach P2

import numpy as _np


def Punkt(x, y):
    """Erstellt einen Punkt mit den Koordinaten (x, y).

    Beispiel:
        P1 = Punkt(0, 0)
        P2 = Punkt(0, 400)
    """
    return _np.array([x, y], dtype=float)


def Vektor(x, y):
    """Erstellt einen Vektor mit den Komponenten (x, y).

    Beispiel:
        v = Vektor(3, 4)   # Zeigt 3 nach rechts und 4 nach oben
    """
    return _np.array([x, y], dtype=float)


def richtungsvektor(P1, P2):
    """Berechnet den Vektor von Punkt P1 zu Punkt P2 (P2 - P1)."""
    return _np.asarray(P2, dtype=float) - _np.asarray(P1, dtype=float)


def vektor_add(v1, v2):
    """Addiert zwei Vektoren (oder verschiebt einen Punkt um einen Vektor)."""
    return _np.asarray(v1, dtype=float) + _np.asarray(v2, dtype=float)


def vektor_sub(v1, v2):
    """Subtrahiert Vektor v2 von Vektor v1 (v1 - v2)."""
    return _np.asarray(v1, dtype=float) - _np.asarray(v2, dtype=float)


def vektor_mal(v, k):
    """Multipliziert Vektor v mit einer Zahl k (Verlängerung/Verkürzung)."""
    return _np.asarray(v, dtype=float) * k


def skalarprodukt(v1, v2):
    """Berechnet das Skalarprodukt (inneres Produkt) zweier Vektoren."""
    v1 = _np.asarray(v1, dtype=float)
    v2 = _np.asarray(v2, dtype=float)
    return float(v1 @ v2)


def kreuzprodukt(v1, v2):
    """Berechnet das 2D-Kreuzprodukt zweier Vektoren.

    Das Ergebnis ist eine Zahl:
    - 0     -> die Vektoren sind parallel (Punkte auf einer Geraden)
    - > 0   -> v2 liegt links von v1 (Gegenuhrzeigersinn)
    - < 0   -> v2 liegt rechts von v1 (Uhrzeigersinn)
    """
    v1 = _np.asarray(v1, dtype=float)
    v2 = _np.asarray(v2, dtype=float)
    return float(v1[0] * v2[1] - v1[1] * v2[0])


def laenge(v):
    """Berechnet die Länge (den Betrag) eines Vektors."""
    return float(_np.linalg.norm(_np.asarray(v, dtype=float)))


def abstand(P1, P2):
    """Berechnet den Abstand zwischen zwei Punkten."""
    return laenge(richtungsvektor(P1, P2))


def einheitsvektor(v):
    """Berechnet den Vektor der Länge 1 mit gleicher Richtung."""
    v = _np.asarray(v, dtype=float)
    l = _np.linalg.norm(v)
    if l == 0:
        raise ValueError("Der Nullvektor hat keine Richtung.")
    return v / l


def normalenvektor(v):
    """Berechnet den Vektor, der senkrecht auf v steht (um 90° gedreht)."""
    v = _np.asarray(v, dtype=float)
    return _np.array([-v[1], v[0]], dtype=float)


def winkel(v1, v2):
    """Berechnet den Winkel zwischen zwei Vektoren in Grad (0 bis 180)."""
    s = skalarprodukt(v1, v2)
    l1 = laenge(v1)
    l2 = laenge(v2)
    if l1 == 0 or l2 == 0:
        raise ValueError("Für den Winkel braucht man Vektoren mit Länge > 0.")
    cos = max(-1.0, min(1.0, s / (l1 * l2)))
    return float(_np.degrees(_np.arccos(cos)))


def mittelpunkt(P1, P2):
    """Berechnet den Mittelpunkt der Strecke zwischen zwei Punkten."""
    P1 = _np.asarray(P1, dtype=float)
    P2 = _np.asarray(P2, dtype=float)
    return (P1 + P2) / 2


if __name__ == "__main__":
    P1 = Punkt(0, 0)
    P2 = Punkt(0, 400)
    P3 = Punkt(400, 0)

    r12 = richtungsvektor(P1, P2)
    r13 = richtungsvektor(P1, P3)
    print(f"r12 = {r12}")
    print(f"r13 = {r13}")
    print(f"Kreuzprodukt: {kreuzprodukt(r12, r13)}")  # != 0 -> nicht kollinear
    print(f"Abstand P1-P3: {abstand(P1, P3)}")
    print(f"Winkel zwischen r12 und r13: {winkel(r12, r13)} Grad")
    print(f"Mittelpunkt P2-P3: {mittelpunkt(P2, P3)}")
