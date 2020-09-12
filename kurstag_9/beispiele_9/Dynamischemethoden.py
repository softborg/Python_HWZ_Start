# coding=utf8
"""
Bei einer Instanz kann ein dynamisches Attribut hinzugefügt werden.
Die Gültigkeit ist je nach Zuordnung - an die Instanz oder an die Klasse
"""


class Konto:

    def __init__(self, inhaber):
        self.inhaber = inhaber


# freie Methode
def freie_methode(self):
    return "Freie Methode"


k = Konto("Max")
print(k.inhaber)

# dynamische Methode an die Klasse (Konto) oder k an die Instanz gebunden gebunden
Konto.freie_methode = freie_methode

print(k.freie_methode())

m = Konto("Fritz")
print(m.inhaber)

print(m.freie_methode())
