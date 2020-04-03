# Statement

# 1 Statement --> eine Aussage
i = 17

# 1 Statement über mehrere Zeilen mit Blacklash (\) kennzeichnen
i = 5 + \
    7
print(i)

# Besondere "Statement" die in runden () , eckingen [] oder geschweiften {} Klammern sind, werden implizit
# über mehrere Zeilen zu einem Statement gepackt

# Runde Klammmern
i = (5
     + 8)
print(i)

# Eckige Klammern --> es entsteht eine Liste: dazu später mehr
i = [5
     + 9]
print(i)

# geschweifte Klammern --> es entsteht eine Dictionary: dazu später mehr
i = {5
     + 10}
print(i)
