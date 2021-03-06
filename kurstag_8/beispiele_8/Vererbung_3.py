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


# Instanziierung eines Sparkonto
# Kontrolle durch den print - Aufruf ("Max")
spar = Sparkonto("Max")
spar.say_hello()
