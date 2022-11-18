import random

class Auto:
    autojen_määrä = 0
    def __init__(self, rekisterinumero, huippunopeus):
        Auto.autojen_määrä = Auto.autojen_määrä + 1
        self.auton_numero = Auto.autojen_määrä
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.ajettu_määrä = 0
    def print_info(self):
        print(f"Auto {self.auton_numero}: {self.rekisterinumero}, huippunopeus: {self.huippunopeus} km/h, kuljettu:{self.ajettu_määrä} km.")


class Sähköauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisterinumero, huippunopeus)

    def print_info(self):
        super().print_info()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti}")

class Polttomoottoriauto(Auto):

    def __init__(self, rekisterinumero, huippunopeus, bensatankinkoko):
        self.bensatankinkoko = bensatankinkoko
        super().__init__(rekisterinumero, huippunopeus)

    def print_info(self):
        super().print_info()
        print(f"Bensatankin koko: {self.bensatankinkoko}")

class Race:
    def __init__(self, pituus, autot):
        self.kilpailun_pituus = pituus
        self.autot = autot
    def auton_nopeus_laskenta(self):

        for auto in self.autot:
            auton_kiihtyvyys = random.randint(10, 70)
            if 0 < auto.nopeus + auton_kiihtyvyys < auto.huippunopeus:
                auto.nopeus = auto.nopeus + auton_kiihtyvyys
            elif auto.nopeus + auton_kiihtyvyys <= 0:
                auto.nopeus = 0
            else:
                auto.nopeus = auto.huippunopeus
    def ajaminen(self):
        for auto in self.autot:
            auto.ajettu_määrä = auto.ajettu_määrä + (auto.nopeus * self.kilpailun_pituus)


autot = []
autot.append(Sähköauto("198-KLO", 190, 52.5))
autot.append(Polttomoottoriauto("944-BCE", 200, 32.3))
autot.append(Sähköauto("192-dsad",190, 32.3))
for t in autot:
    t.print_info()

race = Race(3, autot)
race.auton_nopeus_laskenta()
race.ajaminen()
for t in autot:
    t.print_info()
