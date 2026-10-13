def getBezierPunkte(P1, P2, P3, unterteilungen):
    """Bezier Kurve 2ten Grade mit #unterteilung Punkte"""
    erg = []
    for i in range(unterteilungen + 1):
        t = i / unterteilungen
        erg.append(_bezier(P1, P2, P3, t))
    return erg


def calcBezier(P1, P2, P3, unterteilungen):
    """Bezier Kurve 2ten Grade mit #unterteilung Punkte"""
    t = 0
    while t <= 1:
        P = _bezier(P1, P2, P3, t)
        print(f"{t}: ({P[0]},{P[1]})")
        t += 1 / (unterteilungen)


def _bezier(P1, P2, P3, t):
    """für 0<=t<=1 werden Punkte der Bezier Kurve 2ten Grades berechnet"""
    x = P1[0] * (1 - t) ** 2 + P2[0] * 2 * t * (1 - t) + P3[0] * t**2
    y = P1[1] * (1 - t) ** 2 + P2[1] * 2 * t * (1 - t) + P3[1] * t**2
    return [x, y]


if __name__ == "__main__":
    P1 = [0, 0]
    P2 = [1, 1]
    P3 = [4, 2]
    points = getBezierPunkte(P1, P2, P3, 50)
    for data in points:
        print(data)
