# coding=utf8
"""
Bei einer Instanz kann ein dynamisches Attribut hinzugefügt werden.
Die Gültigkeit ist nur bei dieser Instanz - andere Instanzen verfügen nicht über dieses Attribut
"""


class Konto:

    def __init__(self, inhaber):
        self.inhaber = inhaber


k = Konto("Max")
print(k.inhaber)

# dynamische Attribut an die Instanz gebunden
k.adresse = "8000 Zürich"

print(k.adresse)

m = Konto("Fritz")
print(m.inhaber)
print(m.adresse)  # das Konto m hat keine Adresse !
