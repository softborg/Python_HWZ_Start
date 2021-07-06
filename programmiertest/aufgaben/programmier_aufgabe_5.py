# coding=utf8
# Programmier - Aufgabe 5

"""
# Programmieren sie die Klasse Coordinate aus.
# die Attribute 'breitengrad' und 'laengengrad' sollen als Property zur Verfügung stehen.
# die Zahlenwerte von 'breitengrad' und 'laengengrad' müssen auf ganze Zahlen gerundet werden - siehe auch Asserts
# Die Klasse Coordinate erhält Ortschaft und Land, danach werden Mittels einer URL die Koordinaten dieser Location
# ermittelt und als Breitengrad und Längengard ausgegeben. Wird bei der Instanziierung oder bei der
# Methode get_place nichts mitgegeben, dann soll der Ort=London und das Land uk sein...
# import requests und json sind notwendig, damit die URL bzw. die Response verarbeitet werden kann.
"""

import requests
import json


class Coordinate:
    api_key = ""

    def __init__(self, ort="london", land="uk"):
        pass

    def __get_coordinate(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + self.ort + "," + self.land + "&APPID=" + Coordinate.api_key
        pass

    def get_place(self, ort="london", land="uk"):
        pass


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
if __name__ == '__main__':
    coordinate = Coordinate("Bern", "ch")
    assert coordinate.breitengrad == 47, "Bern Breitengrad: 47"
    assert coordinate.laengengrad == 7, "Bern Längengrad: 7"

    print("Ort: {}, im Land {}, auf dem Breitengrad {} und Laengengrad {}".format(coordinate.ort, coordinate.land,
                                                                                  coordinate.breitengrad,
                                                                                  coordinate.laengengrad))
    coordinate.get_place()
    print("Ort: {}, im Land {}, auf dem Breitengrad {} und Laengengrad {}".format(coordinate.ort, coordinate.land,
                                                                                  coordinate.breitengrad,
                                                                                  coordinate.laengengrad))

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
