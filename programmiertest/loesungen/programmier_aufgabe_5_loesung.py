# coding=utf8
# Programmier - Aufgabe 5

import requests
import json


class Coordinate:
    api_key = ""

    def __init__(self, ort="london", land="uk"):
        self.ort = ort
        self.land = land
        self.__get_coordinate()

    def __get_coordinate(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + self.ort + "," + self.land + "&APPID=" + Coordinate.api_key
        response = requests.get(url)
        data = json.loads(response.text)

        self.ort = data["name"]
        self.land = data["sys"]["country"]
        self.__breitengrad = data["coord"]["lat"]
        self.__laengengrad = round(data["coord"]["lon"])

    def get_place(self, ort="london", land="uk"):
        self.ort = ort
        self.land = land
        self.__get_coordinate()

    @property
    def breitengrad(self):
        return round(self.__breitengrad)

    @property
    def laengengrad(self):
        return round(self.__laengengrad)


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
