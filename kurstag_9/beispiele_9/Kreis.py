# -*- coding: utf-8 -*-
# Properties - dabei handelt es sich um spezielle Deskriptoren
# radius ist ein Attribut
# flaeche und umfang sind Properties - die "passiv" gelesen werden sollen

import math


class Kreis(object):
    def __init__(self, radius):
        self.radius = radius

    # einige zusätzliche Eigenschaften von Circle-Objekten
    @property
    def flaeche(self):
        # Kreisfläche: π * r²
        return math.pi * self.radius ** 2

    @property
    def umfang(self):
        # Kreisumfang: 2 * π * r
        return 2 * math.pi * self.radius


c = Kreis(4.0)
print(c.radius)  # 4.0
print(c.flaeche)  # 50.26548245743669
print(c.umfang)  # 25.132741228718345

# c.flaeche = 2
# Traceback (most recent call last):
#   File '<stdin>', line 1, in <module>
# AttributeError: can't set attribute
# Kein Zugriff möglich, flaeche ist nur ein zu lesendes Property (Attribute)

print(Kreis.flaeche)  # <property object at 0x...>
print(type(Kreis.flaeche))  # <class 'property'>

print(type(Kreis.__init__))  # <class 'function'>
print(Kreis.__init__)  # <function Kreis.__init__ at 0x...>
print(type(c.__init__))  # <class 'method'>
print(c.__init__)  # <bound method Kreis.__init__ of <__main__.Circle object at 0x...>>
