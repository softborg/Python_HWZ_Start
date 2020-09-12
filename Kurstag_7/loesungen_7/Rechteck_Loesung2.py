# coding=utf8

# Aufgabe 1 - Rechteck
# 1. lege eine Klasse 'Rechteck' an
# 2. beim Instanziieren eines Rechtecks sollen 'hoehe' und 'breite' als Parameter mitgegeben werden
# 3. lege 3 Methoden an, set_hoehe(), set_breite() und get_Flaeche(). Die Set-Methoden setzen neue Werte
# die get_Flaeche() solle die Fläche des Rechtecks berechnen und zurückgeben
# 4. Lege eine Instanz Rechteck an
# 5. Gibt die Hoehe und die Breite des Rechtecks aus...
# 6. Verändere beliebig das Rechteck (Höhe oder Breite) - kontrolliere die Fläche jeweils


class Rechteck:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

    def set_hoehe(self,hoehe):
        self.hoehe = hoehe

    def set_breite(self, breite):
        self.breite = breite

    def get_flaeche(self):
        return self.breite * self.hoehe


r = Rechteck(20, 3)
print("Rechteck hat die Breite {} und die Höhe {}, die Fläche ist {} ".format(r.breite, r.hoehe, r.get_flaeche()))

r.set_hoehe(30)
print("Rechteck hat die Breite {} und die Höhe {}, die Fläche ist {} ".format(r.breite, r.hoehe, r.get_flaeche()))

r.set_breite(10)
print("Rechteck hat die Breite {} und die Höhe {}, die Fläche ist {} ".format(r.breite, r.hoehe, r.get_flaeche()))
