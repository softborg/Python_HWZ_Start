import os

# Aktuelles Verzeichnis
aktuelles_verzeichnis = os.getcwd()  # get current work directory getcwd()
print(" Das aktuelle Verzeichnis: {}".format(aktuelles_verzeichnis))

# Welche Dateien gibt es in diesem Verzeichnis
print(" Zeige alle Dateien im aktuellen Verzeichnis: ", os.listdir())

# Verzeichnis wechseln
# os.path.sep = Trennzeichen bei Pfaden (Linux, Windows unterschiedlich)
print("Trennzeichen:" + os.path.sep)
os.chdir(aktuelles_verzeichnis + os.path.sep + "files")
print(os.listdir(os.getcwd()))


