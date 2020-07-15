"""
Eine Familie (1 x Frau = 45 Jahre, 1 x Mann =43 Jahre, 2 Kinder 15 und 17 Jahre alt
möchte den Zoo besuchen, wie hoch sind die Kosten ?
Infos: www.https://www.zoo.ch/de/zoobesuch/tickets-preise

Keine Jahreszeiten, Sonderpreise, Vergünstigungen oder ähnliches berücksichtigen.
Wie teuer kommt der Zoobesuch ?
"""
familie = [45, 43, 15, 17]


def check_range(age):
    if age in range(21, 99):
        print("Erwachsen")
        return 26
    elif age in range(16, 21):
        print("Jugendlich")
        return 21
    elif age in range(6, 16):
        print("Kind")
        return 13
    elif age in range(0, 6):
        print("Baby")
        return 0
    else:
        print("komisch")
        return 1000000


summe = 0.00
for m in familie:
    summe = summe + check_range(m)

print("Familie kostet {:05.2f} CHF ".format(summe))
