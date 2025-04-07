class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        self.regAeg = ""


class Haigla:
    patsientList = []
    arstideList = []

    def patsienditeKuuvamine(self):
        for index, elem in enumerate(self.patsientList):
            print("id: ", index, "Nimi: ", elem.nimi, "Vanus: ", elem.vanus)

    def arstideKuuvamine(self):
        for index, elem in enumerate(self.arstideList):
            print("id: ", index, "Nimi: ", elem.nimi, "Vanus: ", elem.vanus, "Eriala: ", elem.eriala)

    def kohtumineTegimine(self):
        patsientIndex = 0
        patsientiNimi = input("Sisesta patsienti nimi: ")
        arstiNimi = input("Sisesta arsti nimi: ")

        patsient = None
        arst = None

        for elem in self.patsientList:
            if elem.nimi == patsientiNimi:
                patsient = elem
                patsientIndex = self.patsientList.index(elem)

        for elem in self.arstideList:
            if elem.nimi == arstiNimi:
                arst = elem

        if patsient and arst:
            print(f"Patsient {patsient.nimi} ja arst {arst.nimi} on leitud.")
            print("Arsti vaba aeg: ", arst.aeg)

            aeg = input("Vali aeg (näiteks 10.40, 13.30): ")
            if aeg in arst.aeg:
                patsient.regAeg = aeg
                arst.aeg.remove(aeg)
                print(f"Patsient {patsient.nimi} on registreeritud ajaks {aeg}.")
            else:
                print("Valitud aeg ei ole saadaval.")
        else:
            print("Patsienti või arsti ei leitud.")


class Arst:
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = aeg


Patsient1 = Patsient("Kiril", 42)
Patsient2 = Patsient("Mart", 36)
Arst1 = Arst("Artur", 58, "Kirurg", [10.40, 13.30, 16.20])

haigla = Haigla()

haigla.patsientList.append(Patsient1)
haigla.patsientList.append(Patsient2)
haigla.arstideList.append(Arst1)

haigla.patsienditeKuuvamine()
haigla.arstideKuuvamine()

haigla.kohtumineTegimine()
