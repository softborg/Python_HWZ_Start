""" 
Zeit Aufgabe 01

Bilden sie aus ihrem Geburtsdatum als String ein DateTime Objekt
gebdatum = "01.01.2000" --> Konvertieren...

"""

# Zeit Aufgabe 01 - Lösung

from datetime import datetime

gebdatum = '30.09.2018'

date_object = datetime.strptime(gebdatum, '%d.%m.%Y').date()
print(type(date_object))
print(date_object)  # printed in default formatting
