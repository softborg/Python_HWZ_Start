# coding=utf8
# Aufgabe 1 - Rechteck
# 1. lege eine Klasse 'Rechteck' an
# 2. beim Instanziieren eines Rechtecks sollen 'hoehe' und 'breite' als Parameter mitgegeben werden
# 3. Lege eine Instanz Rechnteck an
# 4. Gibt die Hoehe und die Breite des Rechtecks aus...


class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe


r = Rechteck(200, 300)
print("Rechteck hat die Breite {} und die Höhe {}".format(r.breite, r.hoehe))
