# coding=utf8

# Aufgabe 1 - Magische Methode Aufgabe 1
# 1. Erstellen sie eine Klasse Vector
# 2. Beim Instanziieren geben sie 'x', 'y', und 'z' - alle public als mit
# 3. Schreiben sie eine "magische Methode", die Vector (1,2,5) + Vector (2,3,4) korrekt zusammenzählt

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, + self.z)


vector3 = Vector(1, 2, 5) + Vector(2, 3, 4)

print(vector3)
print(Vector(1, 2, 5) + Vector(2, 3, 4))
