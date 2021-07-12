class Mobile:
    nord = "Norden"
    east = "Osten"
    south = "Süden"
    ouest = "Westen"

    def drive(self):
        print("ich fahre")

    def brake(self):
        print("ich bremse")


class Car(Mobile):

    def __init__(self, gear=1):
        self.__gear = gear

    def drive(self):
        print("ich fahre auf der Strasse")

    def set_gear(self, gear):
        self.__gear = gear
        print("Gang ", self.__gear, "eingelegt")


class Ship(Mobile):

    def __init(self, way=Mobile.nord):
        self.__way = way

    def drive(self):
        print("ich schwimme")

    # def neue Methode nur in der Ship Klasse
    def set_way(self, way):
        self.__way = way
        print("ich fahre nach", self.__way)


fahrzeuge = [Car(), Ship(), Car(), Car()]

for fahrzeug in fahrzeuge:
    fahrzeug.drive()

    if isinstance(fahrzeug, Car):
        fahrzeug.set_gear(2)

    # nur Ship Methode aufrufen
    if isinstance(fahrzeug, Ship):
        fahrzeug.set_way(Mobile.east)

for fahrzeug in fahrzeuge:
    fahrzeug.brake()
