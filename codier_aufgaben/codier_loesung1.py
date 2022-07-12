"""
Programmierung sie eine Funktion “besitzer_files”:
z.b die Übergabe ist ein Dictionary {'Bild1.jpg': 'Markus', 'Car.py': 'Petra', 'text.doc': 'Markus'}
Die Funktion muss folgende Rückgabe machen {'Markus': ['Bild1.jpg', 'text.doc'], 'Petra': ['Car.py']}.
Vorgabe:
files = {
       'Bild1.jpg': 'Markus',
       'Car.py': 'Petra',
       'text.doc': 'Markus'
   }
   print(besitzer_files(files))

Verlangte Ausgabe: {Markus: ['Bild1.jpg', 'text.doc'], 'Petra': [Car.py']}

 """


def besitzer_files(dateien):
    owner = {}
    for key, value in dateien.items():
        if value not in owner:
            owner[value] = [key]
        else:
            owner[value].append(key)
    return owner


files = {
    'Bild1.jpg': 'Markus',
    'Car.py': 'Petra',
    'text.doc': 'Markus'
}
print(besitzer_files(files))