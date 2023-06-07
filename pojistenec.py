class Pojistenec:

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.telefon}, {self.vek}"

    def pridej_pojisteneho(self):
        self.jmeno = input("Zadejte jméno pojištěného:\n")
        self.prijmeni = input("Zadejte příjmení pojištěného:\n")
        self.telefon = input("Zadejte telefonní číslo:\n")
        self.vek = input("Zadejte věk:\n")