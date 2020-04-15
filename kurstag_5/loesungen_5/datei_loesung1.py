"""
Datei Aufgabe 01

Schreiben sie in eine Datei 'hauptstadt.txt
Jeder Werte einzeln in Datei: orte = ['Rom', 'Paris']
Öffnen sie Datei mit "with und Schreiboption 'w'
Anschliessend schliessen sie die Datei

"""
# Datei Aufgabe Lösung 1

orte = ['Rom', 'Paris']
with open('hauptstadt.txt', "w") as f:
    # write file content
    for ort in orte:
        f.write('%s\n' % ort)

if not f.closed:
    print('File is not closed')
else:
    print('File is closed')