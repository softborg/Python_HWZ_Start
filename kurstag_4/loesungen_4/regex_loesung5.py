# Aufgabe 05
# Filtere alle Files aus, die mit File beginnen
# und mit der Extension PDF oder Doc enden
# Vorgabe:
# files = ["File_today.pdf","File_21022099.pdf","file.txt",
#         "File_Bild.jpg","File.doc", "Temp_File.doc"]


# Aufgabe 05 - Lösung
import re

files = ["File_today.pdf", "File_21022099.pdf", "file.txt",
         "File_Bild.jpg", "File.doc", "Temp_File.doc"]

for f in files:
    match = re.search("^(File).*(.pdf$|.doc$)", f)
    if match is not None:
        print(match.group())
