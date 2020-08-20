# coding=utf8
# Fit 7

from datetime import datetime


def date_time(time: str) -> str:

    # Programmier - Aufgabe 7
    # Input: String (Datum)
    # Bedingung : Ausgabeformat einhalten
    # Output: Datum als String gemäss Formatsvorgaben

    date_time_obj = datetime.strptime(time, '%d.%m.%Y %H:%M')
    date_object = datetime.strftime(date_time_obj, '%d %B %Y year %H hours %M minutes').lstrip("0").replace(" 0", " ")

    if int(date_time_obj.hour) == 1:
        date_object = date_object.replace("hours", "hour")
    if int(date_time_obj.minute) == 1:
        date_object = date_object.replace("minutes", "minute")

    return date_object


if __name__ == '__main__':
    print("Beispiel Datum formatieren:")
    print(date_time('01.01.2000 00:00'))
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
