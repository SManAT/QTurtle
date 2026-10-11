def bezier(P1, P2, P3, t):
    """für 0<=t<=1 werden Punkte der Bezier Kurve 2ten Grades berechnet"""
    x = P1[0] * (1 - t) ** 2 + P2[0] * 2 * t * (1 - t) + P3[0] * t**2
    y = P1[1] * (1 - t) ** 2 + P2[1] * 2 * t * (1 - t) + P3[1] * t**2
    return [x, y]


if __name__ == "__main__":
    P1 = [0, 0]
    P2 = [1, 1]
    P3 = [4, 2]

    t = 0
    while t <= 1:
        P = bezier(P1, P2, P3, t)
        print(f"{t}: ({P[0]},{P[1]})")
        t += 0.5
