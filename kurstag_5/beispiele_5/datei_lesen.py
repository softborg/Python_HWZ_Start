# Die einfachste Art eine Datei zu lesen
meine_datei = open("test.txt")  # Öffnet eine Datei im aktuellen Verzeichnis

inhalt = meine_datei.read()  # liest die Datei aus
print("Der Datei - Inhalt: " + inhalt)  # Ausgabe der Datei


# Wäre die Datei nicht vorhanden, dann gäbe es einen Fehler
# Darum ist es besser die Datei mit einer Fehlerbehandlung zu lesen

file_name = "unbekannte.txt"
try:
    with open(file_name)as zweite_datei:
        print(zweite_datei.read())
except FileNotFoundError:
    print("Datei {} konnte nicht gefunden werden".format(file_name))

