# Basisklasse (leer)
class Konto:
    pass


# Subklasse die von Konto erbt (leer)
class Sparkonto(Konto):
    pass


# Instanziierung eines Sparkonto
# Kontrolle durch den print (<__main__.Sparkonto object at 0x01861880>)
spar = Sparkonto()
print(spar)
