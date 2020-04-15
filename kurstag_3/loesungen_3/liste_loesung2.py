"""
Liste Aufgabe 02
2 Listen sind Given a two list.
Create a third list by picking an odd-index element from the first list and even index elements from second.

Vorgegeben sind diese 2 Listen:
liste1 = [3, 6, 9, 12, 15, 18, 21]
liste2 = [4, 8, 12, 16, 20, 24, 28]

liste3 solle von liste1 alle gerade Elemente übernehmen (0,2,4,...)
und von liste2 alle ungeraden Elemente (1,3,5...) übernehmen

"""

# Liste Aufgabe 02 - Lösung

liste1 = [3, 6, 9, 12, 15, 18, 21]
liste2 = [4, 8, 12, 16, 20, 24, 28]

liste3 = liste1[1::2] + liste2[0::2]

print(liste3)