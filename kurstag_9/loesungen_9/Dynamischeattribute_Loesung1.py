# coding=utf8

# Aufgabe 1 - Dynamische Attribute
# 1. Erstellen sie eine Klasse Buch
# 2. Beim Instanziieren geben sie titel (public) und preis (public) mit
# 3. Legen sie eine Instanz Buch an
# 4. Fügen sie ein dynamisches Attribut 'bemerkung' an die die Instanz an
# 5. Geben sie alle 3 Werte aus (titel, preis) und bemerkung
# 6. Für den Test: legen sie eine weiter Instanz an und versuchen sie die Bemerkung auszugeben
# 7. Wiederholen sie die Schritte 4-6 nochmals mit dem Unterschied, dass sie die Bemerkung der Klasse Buch anfügen
# 8. Was fällt auf ?


class Buch:
    def __init__(self, titel:str, preis:float):
        self.titel = titel
        self.preis = preis


buch = Buch("Python 3, Einsteigen und Durchstarten", 30)

buch.bemerkung = "Jetzt ist alles klar"

print(buch.titel, buch.preis, buch.bemerkung)


buch2 = Buch("Python 3, Einsteigen und Durchstarten", 30)
print(buch2.titel, buch2.preis, buch2.bemerkung)
