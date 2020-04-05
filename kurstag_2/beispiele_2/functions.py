# Funktionen: 1 - n Statements über einen Namen ansprechen
# Keyword def name(optional Argumente):
# kann etwas zurückgeben


def gruss():
    print("Herzlich Willkommen")
    print("zum Kurz Python_HWZ_Start")


# Funktion aufrufen
gruss()

print('-' * 32)


# Funktion mit def "addieren" Runde Klammern, Parameter, Schliessende Runde Klammer, Doppelpunkt
def addieren(a, b):
    return a + b


# Aufruf einer Funktion 2 Paramertern und 1 Rückgabewert
print(addieren(4, 5))

print('-' * 32)


# Funktion mit lokalen Variablen
def calc_CH(nettopreis):
    mwst = 7.7  # lokale Variable
    return nettopreis * (100 + mwst) / 100


preis = 100
mwst = 19  # globale Variable

bruttopreis = calc_CH(preis)

#
print(bruttopreis)

print('-' * 32)


# Funktion willkommen, mit 1 Muss Parameter und 1 kann Parameter.
# Aufrufe mit nur 1 Parameter, dann wird der Default Wert genutzt
def willkommen(name, msg="Welcome !"):
    print("Hallo", name + ', ' + msg)


willkommen("Robert")
willkommen("Peter", "Willkommen !")

# Auch benannte Parameter sind möglich, Reihenfolge kann gedreht werden
willkommen(name="Pierre", msg="Bienvenue ")
willkommen(msg="Bienvenuti ", name="Piero")

print('-' * 32)


# mit einem * kann einer beliebigen Anzahl Parameter übergeben werden (wird als 'tuple' übernommen')
def ciao(*names):

    for name in names:
        print(" Auf Wiedersehen", name)


ciao("Robert", "Peter", "Pierre", "Piero")
