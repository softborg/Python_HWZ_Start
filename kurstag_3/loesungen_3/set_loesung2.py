"""
 Set Aufgabe 02

 Einem Farben Set soll eine Farbenliste übergeben werden

 farbenset = blau, gelb, rot
 farbenliste = braun, violet, rosa, schwarz

 Anzeige:

"""

# Set Aufgabe 02 - Lösung

farbenset = {'blau', 'gelb', 'rot'}
farbenliste = ['braun','violet','rosa','schwarz']
farbenset.update(farbenliste)

print(farbenset)