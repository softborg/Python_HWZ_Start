# coding=utf8
# Programmier - Aufgabe 4 - Lösung


def sonnenstand(time):

    """
    time enthält eine Uhrzeit im Format hh:mm
    Mit dem Sonnenstand lässt sich Uhrzeit bestimmen:
    um 06:00 steht die Sonne bei 0 Grad --> geben sie den Wert 0 zurück
    um 12:00 steht die Sonne bei 90 Grad --> geben sie den Wert 90 zurück
    um 18:00 steht die Sonne bei 180 Grad -- geben sie den Wert 180 zurück
    Zeiten ausserhalb von 06:00 - 18:00 ---> Keine Sonne zurückgeben
    """

    stunden = int(time.split(":")[0])
    minuten = int(time.split(":")[1])
    if 5 < stunden < 19:
        if stunden == 18 and minuten != 0:
            return "Keine Sonne!"
        if minuten == 0:
            return (stunden - 6) * 15
        else:
            return (stunden - 6) * 15 + 15 / 60 * minuten
    else:
        return "Keine Sonne!"


if __name__ == '__main__':
    print("Sonnenstand:")
    print(sonnenstand("07:00"))

    # Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
    assert sonnenstand("07:00") == 15
    assert sonnenstand("12:15") == 93.75
    assert sonnenstand("15:45") == 146.25
    assert sonnenstand("18:01") == "Keine Sonne!"
    assert sonnenstand("06:15") == 3.75
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")