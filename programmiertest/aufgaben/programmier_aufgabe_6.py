# coding=utf8
# Programmier - Aufgabe 6

"""
Ergänzen sie die Variante PDF im Sinne des Codes.
Keine Veränderung am bestehenden Code, nur Ergänzungen

"""


class Document:
    def show(self):
        print("is not implemented yet xxx")


class ODFDocument(Document):
    def show(self):
        print('Open document format')
        return "odf"


class MSOfficeDocument(Document):
    def show(self):
        print('MS Office document format')
        return "doc"


class Application:
    def create_document(self, type_):
        print("existiert nicht")


class MyApplication(Application):
    def create_document(self, type_):
        if type_ == 'odf':
            return ODFDocument()
        elif type_ == 'doc':
            return MSOfficeDocument()
        else:
            return Document()


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
if __name__ == '__main__':
    app = MyApplication()
    assert app.create_document('odf').show() == "odf", "korrekte odf Anzeige "
    assert app.create_document('doc').show() == "doc", "korrekte doc Anzeige "
    assert app.create_document('pdf').show() == "pdf", "korrekte pdf Anzeige "

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
