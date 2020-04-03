# Gültige Variablen Namen

# 1. beginnt mit Buchstaben (a - z) oder (A-Z) oder mit _ --> Unterstrich
# 2. Zahlen sind ab der 2.ten Stelle erlaubt
# 3. lange Variablen werden am Besten mit Unterstrich verbunden --> Snake_typing
# 4. Gross-und Kleinschreibung wird unterschieden: a ungleich A !
# 5. Variablen die nur aus Grossbuchstaben bestehen, werden als Konstanten gesehen (Konvention) !!

# gute Variablen

i = 1
mwst = 7.7
buch_titel = 'Python'

# nicht zu empfehlen

ä = 1  # ---> was geschieht, wenn kein ä vorhanden ist auf dem Computer
MEHRWERTUmsatzSTEUER = 7.7  # sehr schwer zu lesen ---> besser ist: mehrwertsteuer oder mehr_wert_steuer

# Was nicht geht
# 1juni --> darf nicht mit Zahl beginnen
#

# Konstante definieren - leider kein spezieller Schutz möglich - einfach Konvention

ZH = "Zürich"  # --> Wert als Konstante "anerkennen" - ändern dennoch möglich
ZH = "Zentralheizung"
print(ZH)  # Wert ist Zentralheizung

