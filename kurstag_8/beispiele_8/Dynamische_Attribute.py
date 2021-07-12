# coding=utf8
"""
Basisklasse mit
1 Instanzvariable (public Attribut)
1 Methode
"""


class Konto:
    def __init__(self, inhaber):
        self.inhaber = inhaber

    def say_hello(self):
        print("Hallo, ich bin", self.inhaber)


# Subklasse die von Konto erbt
class Sparkonto(Konto):
    pass


# Instanziierung 2 Sparkonti
spar_max = Sparkonto("Max")
spar_urs = Sparkonto("Urs")

# "feste Instanzattribute abfragen
print(spar_max.inhaber)
print(spar_urs.inhaber)

# dynamisches Attribut einer Instanz hinzufügen
spar_max.alter = 30

print(spar_max.alter)

# print(spar_urs.alter) --> führt zu Fehler
# diese Instanz hat das dynamische Attribut Alter nicht
print(spar_urs.alter)

