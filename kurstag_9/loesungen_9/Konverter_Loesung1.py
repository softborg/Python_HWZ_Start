# coding=utf8

# Aufgabe 1 - Celsius
# 1. erstellen sie eine Klasse 'Celsius'
# 2. beim Instanziieren soll die Temperatur in Celsius mitgegeben werden
# 3. Die Temperatur ist proteced
# 4. Die Klasse kann die Temperatur in Fahrenheit ausgeben. Formel x* 1.8 + 31
# 5. Die Zugriff auf Temperatur via getter() und setter() Methode, die mit Property (old-style) gebunden wird
# 6. Die Setter - Methode validiert, ob der Wert als 273 Grad Celsius ist, wenn tiefer --> Error werfen
# 7. Testen sie diese Klasse mit diversen Ausgaben (Celsius und Fahrenheit), ändern sie Temperatur


class Celsius:
    def __init__(self, temperature):
        self._celsius = temperature

    def to_fahrenheit(self):
        return self._celsius * 1.8 + 32

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, temp):
        if temp < -273:
            raise ValueError("Temperaturen kälter als -273 sind unmöglich")
        self._celsius = temp

    property(get_celsius, set_celsius)


c = Celsius(0)
print(c.to_fahrenheit())

c.celsius = 20
print(c.to_fahrenheit())
print(c.celsius)
