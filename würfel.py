import random

class Wuerfel:
    def __init__(self):
        self.seiten = 6

    def würfeln(self):
        return random.randint(1, self.seiten)

def würfeln_bis_6(wuerfel):
    augenzahl = wuerfel.würfeln()
    würfel_zähler = 1
    while augenzahl != 6:
        augenzahl = wuerfel.würfeln()
        würfel_zähler += 1
    return würfel_zähler


wuerfel = Wuerfel()
würfel_zähler = würfeln_bis_6(wuerfel)

print("Du hast", würfel_zähler, "Versuche nötigt, um eine 6 zu würfeln.")
