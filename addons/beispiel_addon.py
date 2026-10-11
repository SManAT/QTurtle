# Beispiel-Addon für QTurtle
#
# Jede .py-Datei in diesem Ordner wird beim Start eines Skripts geladen.
# Alle Funktionen, Klassen und Variablen ohne führenden Unterstrich ("_")
# sind danach direkt im Skript verfügbar - ganz ohne import:
#
#     from qturtle_app.lib...  # nicht nötig
#     stern(t, 100)            # reicht!


def stern(t, laenge=100, zacken=5):
    """Zeichnet einen Stern mit der Turtle t."""
    winkel = 720 / zacken
    for _ in range(zacken):
        t.forward(laenge)
        t.right(winkel)


def vieleck(t, seiten=6, laenge=80):
    """Zeichnet ein regelmäßiges Vieleck mit der Turtle t."""
    winkel = 360 / seiten
    for _ in range(seiten):
        t.forward(laenge)
        t.right(winkel)
