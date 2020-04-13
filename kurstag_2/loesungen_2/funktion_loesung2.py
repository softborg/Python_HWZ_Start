"""
Funktion Aufgabe 02
Sparbuch:
Schreiben Sie ein Funktion die mit Startkapital, Zinssatz und Laufzeit
Jedes Jahr Startwert, Zins Endwert nach x. Jahr auf dem Bildschirm ausgibt.
Der Wert des Geldbetrags erhöht sich jedes Jahr um den Faktor:
 (100.0 + zinssatz) / 100 """


def sparbuch(startkapital, zinsrate, laufzeit):
    print("Startkapital:", startkapital, "Zins:", zinsrate, "%", "Laufzeit:", laufzeit, "Jahre\n")
    for i in range(1, laufzeit + 1):
        zins = startkapital * (100 + zinsrate) / 100 - startkapital
        startkapital += zins
        print("Kapital: {kap:.2f} Zins:{zins:.2f} Laufzeit:{jahr}.Jahr".format(kap=startkapital, zins=zins, jahr=i))


sparbuch(1000, 3, 25)
