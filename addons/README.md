# Addons

Lege hier eigene Python-Dateien (`.py`) ab. Beim Start jedes Skripts lädt QTurtle
alle Dateien aus diesem Ordner und stellt deren öffentliche Funktionen, Klassen
und Variablen direkt im Skript zur Verfügung — ganz ohne `import`.

## Regeln

- Der Dateiname wird zum Modulnamen (`stern.py` → Modul `stern`).
- Namen mit führendem Unterstrich (`_privat`) werden nicht exportiert.
- Dateien, die mit `_` beginnen, werden ganz übersprungen.
- Ein Fehler in einer Addon-Datei bricht das Skript nicht ab; es erscheint nur
  eine Warnung in der Konsole.
- Spätere Schülerdefinitionen im Skript überschreiben Addon-Namen.

Im ausführbaren Build (cx_Freeze/PyInstaller) liegt der Ordner einfach neben
der `QTurtle.exe`.

## Beispiel

`beispiel_addon.py` definiert `stern(t, laenge, zacken)` und
`vieleck(t, seiten, laenge)`. Im Editor genügt dann:

```python
import turtle

t = turtle.Turtle()
stern(t, 100)      # ohne import direkt verwendbar
turtle.done()
```
