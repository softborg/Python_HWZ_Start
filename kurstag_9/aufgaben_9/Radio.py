class Radio:
    def __init__(self, volume):
        self.volume = volume

        # hier wird das 'volume' dem Property Wert self.volume zugewiesen
        # - implizit wird die Methode set_Volume aufgerufen
        # somit kann das Radio auch beim Instanziieren keinen grösseren Wert als 100 zulassen.
        # kein Weg "ungültige Werte" dem Radio mitzugeben. bei der init Funktion und beim Zugriff geregelt

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        if volume <= 100:
            self.__volume = volume
        else:
            raise ValueError("max value is 100")

    volume = property(get_volume, set_volume)


r = Radio(20)
r.volume = 80
print(r.volume)