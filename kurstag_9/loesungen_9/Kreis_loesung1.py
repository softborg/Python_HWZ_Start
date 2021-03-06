# coding=utf8

# Aufgabe 1 - Kreis
# 1. erstellen sie folgende Klasse 'Kreis
# 2. beim Instanziieren soll der Radius mitgegeben werden, der Radius ist public
# 3. Definieren sie ein Klassenvariable pi = 3.1
# 4. Berechnen sie die Fläche in einer Methode und geben diesen Wert zurück
# 5. Geben sie beim Testen den Wert von Pi aus...
# 6. Instanziieren sie nun 2 Kreise mit unterschiedlichen Werten
# 7. Drucken von beiden die Fläche aus
# 8. Ändern nun den Wert von pi auf = 3.1415
# 9. Drucken von beiden die Fläche erneut aus aus


class Kreis:
    pi = 3.1

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Kreis.pi * self.radius * self.radius


print(Kreis.pi)

k = Kreis(10)
k2 = Kreis(20)

print(k.area(), k2.area())

Kreis.pi = 3.14159

print(k.area(), k2.area())
