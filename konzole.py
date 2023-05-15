from pojisteni import Databaze

db = Databaze()


class Konzole:

    def pracuj(self):
        print("---------------------")
        print("Evidence pojištěných")
        print("---------------------")

        print("Vyberte si akci:")

        vstup = 0

        while vstup != 4:
            try:
                vstup = int(input("1 - Přidat nového pojistného\n2 - Vyhledat všechny pojištěné\n3 - Vyhledat pojištěného\n4 - Konec\n"))
                if vstup == 1:
                    db.pridej_pojisteneho()
                    print("\nData byla vložena do databáze!\n")
                    continue
                elif vstup == 2:
                    db.vrat_pojistene()
                    print("")
                elif vstup == 3:
                    db.vyhledej_pojisteneho()
                    print("")
                else:
                    print("Sbohem!")
                    break
            except ValueError as ve:
                print("Zadejte číslo!\n")