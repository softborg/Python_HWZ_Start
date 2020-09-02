# Basisklasse mit 1 Instanzvariable (public Attribute)
class Konto:
    def __init__(self, inhaber):
        self.inhaber = inhaber


# Subklasse die von Konto erbt
class Sparkonto(Konto):
    pass


# Instanziierung eines Sparkonto
# Kontrolle durch den print - Aufruf ("Max")
spar = Sparkonto("Max")
print(spar.inhaber)


