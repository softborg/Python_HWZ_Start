class BasicPlan:
    price = 8.99
    num_of_devices = 1

    def __init__(self, can_stream, can_download,has_SD):
        self.can_stream = can_stream
        self.can_download = can_download
        self.has_SD = has_SD


class StandardPlan(BasicPlan):
    price = 12.99
    num_of_devices = 2

    def __init__(self, can_stream, can_download,has_SD, has_HD):
        # Super...
        self.has_HD = has_HD


class PremiumPlan(StandardPlan):
    price = 15.99
    num_of_devices = 4

    def __init__(self, can_stream, can_download,has_SD, has_HD, has_UHD):
        # Super...
        self.has_UHD = has_UHD


print(BasicPlan.has_SD)

print(PremiumPlan.has_SD)

print(BasicPlan.has_UHD)

print(BasicPlan.price)

print(PremiumPlan.num_of_devices)