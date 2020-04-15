"""
Datei Aufgabe 02

Öffnen sie die Datei 'hauptstadt.txt
Und hängen nun die Werte der Datei an: orte = ['Berlin', 'Prag']
Öffnen sie Datei mit "with und Schreiboption 'a'
Anschliessend schliessen sie die Datei

"""
# Datei Aufgabe Lösung 2

orte = ['Berlin', 'Prag']
with open('hauptstadt.txt', "a") as f:
    # write file content
    for ort in orte:
        f.write('%s\n' % ort)

if not f.closed:
    print('File is not closed')
else:
    print('File is closed')