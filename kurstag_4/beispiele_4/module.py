# Module referernzieren auf ein Pyton File dieses enthält statements und Defintionen
# beispiel.py ist ein Modul und das Modul heisst: beispiel

# mittels import kann ich das Module beispiel genutzt werden
from kurstag_4.beispiele_4 import beispiel

print(beispiel.addieren(2, 3))

# Standart Modul # laut PEP immer am Anfang des Files stehen.
import math

print(math.pi)

# * ist eine Wildkarte hier werden alle Programmteile eingefügt.
from math import *

print(pi)

# referenzieren, import funktion as rename (Kurzname)
from kurstag_4.beispiele_4.beispiel import addieren as summe

print(summe(3, 3))
