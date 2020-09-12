class Mobile:

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

    def drive(self):
        print("ich schwimme")


fahrzeuge = [Car(), Ship(), Car(), Car()]

for fahrzeug in fahrzeuge:
    fahrzeug.drive()

    if isinstance(fahrzeug, Car):
        fahrzeug.set_gear(2)

for fahrzeug in fahrzeuge:
    fahrzeug.brake()
