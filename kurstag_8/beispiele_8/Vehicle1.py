class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


v = Vehicle(100, 3000)
print(v.max_speed, v.mileage)
