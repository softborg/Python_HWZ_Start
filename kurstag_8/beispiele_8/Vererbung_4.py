"""
Basisklasse mit
1 Instanzvariable (public Attribut)
1 Methode + 1 Methode
Subklasse mit 1 Methode - die die Methode
der Basisklasse überschreibt
"""


class Konto:
    def __init__(self, inhaber):
        self.inhaber = inhaber

    def say_hello(self):
        print("Hallo, ich bin", self.inhaber)


# Subklasse die von Konto erbt
class Sparkonto(Konto):

    def say_hello(self):
        print("Hello, i am", self.inhaber)


# Instanziierung eines Sparkonto
# Kontrolle durch den print - Aufruf ("Max")
spar = Sparkonto("Max")
spar.say_hello()
