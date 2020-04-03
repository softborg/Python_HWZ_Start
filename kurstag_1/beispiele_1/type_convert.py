# mit type(xxx) lässt sich feststellen, welcher Datentyp vorliegt

i = 1
print(type(i))  # <class type 'int'>

f = 37.999
print(type(f))  # <class type 'float'>

x = 4.0j
print(type(x))  # <class type 'complex'>

f2 = float(i)
print(type(f2), f2)  # der Wert aus i wir explizit konvertiert, alles i.0

i2 = int(f)
print(type(i2), i2)  # der Wert aus f wir explizit konvertiert, Informationsverlust: Kommastellen werden 'abgeschnitten'

str1 = '1'
i3 = int(str1)
print(type(i3), i3)  # aus einem String ist ein 'int' geworden

str2 = '2.0'
i3 = float(str2)
print(type(i3), i3)  # aus einem String ist ein 'float' geworden

"""
str3 = 'a'
i3 = float(str3)
print(type(i3), i3)  # aus einem String zu float: Fehler--> 'a' ist keine Zahl.
"""
