# coding=utf8

# Aufgabe 1 - Dynamische Methode
# 1. Erstellen sie eine Klasse Buch
# 2. Beim Instanziieren geben sie titel (public) und preis (public) mit
# 3. Legen sie eine Instanz Buch an
# 4. Fügen sie eine dynamisches Methode 'rabatt' die nur die Zahl 50 zurück gibt an die die Instanz an
# 5. Geben sie alle 3 Werte aus (titel, preis) und rabatt
# 6. Für den Test: legen sie eine weiter Instanz an und versuchen sie den Rabatt auszugeben
# 7. Wiederholen sie die Schritte 4-6 nochmals mit dem Unterschied, dass sie die Rabatt der Klasse Buch anfügen
# 8. Was fällt auf ?


class Buch:
    def __init__(self, titel: str, preis: float):
        self.titel = titel
        self.preis = preis


def rabatt():
    return 50


buch = Buch("Python 3, Einsteigen und Durchstarten", 30)

Buch.rabatt = rabatt()

print(buch.titel, buch.preis * buch.rabatt / 100)

b = Buch("asdf",8)
print (b.rabatt)