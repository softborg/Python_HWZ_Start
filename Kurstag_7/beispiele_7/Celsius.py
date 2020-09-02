# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def hugo(self):
        print("Getting value...")
        return self._temperature

    @hugo.setter
    def hugo(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value




# create an object
human = Celsius(37)

print(human.hugo)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)