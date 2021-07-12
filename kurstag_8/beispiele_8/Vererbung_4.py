# coding=utf8
"""
Basisklasse mit
1 Instanzvariable (public Attribut)
1 Methode + 1 Methode
Subklasse mit 1 Methode - die die Methode
der Basisklasse �berschreibt
"""


class Konto:
    def __init__(self, inhaber):
        self.inhaber = inhaber

    def say_hello(self):
        print("Hallo, ich bin", self.inhaber)


# Subklasse die von Konto erbt
class Sparkonto(Konto):

    def __init__(self, inhaber, saldo=0):
        super().__init__(inhaber)
        self.saldo = saldo

    def say_hello(self):
        print("Hello, i am", self.inhaber)

    def __str__(self):
        return "Sparkasse - Inhaber {} mit Saldo: {} ".format(self.inhaber, self.saldo)


# Instanziierung eines Sparkonto
# Kontrolle durch den print - Aufruf ("Max")
spar = Sparkonto("Max")
spar.say_hello()
print(spar.saldo)
print(spar)
