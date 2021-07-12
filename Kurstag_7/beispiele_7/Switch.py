# -*- coding: utf-8 -*-
class Switch:
    def __init__(self):
        self.state = False

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def is_on(self):
        return self.state


s1 = Switch()
print(s1)

s2 = Switch()
print(s2)

s3 = s1
print(s3)

s1.on()
print(s3.is_on()) # Was ist die Ausgabe ? --> Vermutung ist: True
