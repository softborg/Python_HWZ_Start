# coding=utf8
# Programmier - Aufgabe 7

"""
# dictionaries können mit 'update' zu einem dictonary verbunden werden

dict1 = {1: "ABC"}
dict2 = {2: "EFG"}

# updates the value of key 2
dict1.update(dict2)
print(dict1)

Schreiben sie eine Klasse die von 'dict' ableitet und implementieren sie eine
Methode die ihnen folgendes erlaubt:

dict3 = dict1 + dict2
print(dict3) # {1: 'ABC', 2: 'EFG'}

"""


class MyDict(dict):

    def __add__(self, other):
        self.update(other)
        return MyDict(self)


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
if __name__ == '__main__':
    dict1 = MyDict({1: "ABC"})
    dict2 = MyDict({2: "EFG"})

    assert dict1 + dict2 == {1: 'ABC', 2: 'EFG'}

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")