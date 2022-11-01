class Julkaisu:
    julkaisujen_määrä = 0
    def __init__(self, nimi):
        Julkaisu.julkaisujen_määrä = Julkaisu.julkaisujen_määrä + 1
        self.julkaisun_numero = Julkaisu.julkaisujen_määrä
        self.nimi = nimi
    def print_info(self):
        print(f"{self.julkaisun_numero}. Julkaisu: {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def print_info(self):
        super().print_info()
        print(f"Kirjan kirjoittaja: {self.kirjoittaja}. ")
        print(f"Kirjan sivumäärä: {self.sivumäärä}.")
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def print_info(self):
        super().print_info()
        print(f"Lehden päätoimittaja: {self.päätoimittaja}. ")

julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom",200))
julkaisut.append(Lehti("Aku ankka", "Aki hyppääjä"))

for t in julkaisut:
    t.print_info()
