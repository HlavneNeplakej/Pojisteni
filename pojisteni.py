import sqlite3
conn = sqlite3.connect('uzivatele.db')
cur = conn.cursor()
cur.execute('SELECT count(name) FROM sqlite_master WHERE type="table" AND name="pojistenci"')

if cur.fetchone()[0] == 1:
    pass
else:
    cur.execute('CREATE TABLE "pojistenci" ("pojistenec_id" INTEGER PRIMARY KEY AUTOINCREMENT, "jmeno" TEXT, '
                '"prijmeni" TEXT, "telefon" INTEGER, "vek" INTEGER);')
    conn.commit()


class Databaze:

    def pridej_pojisteneho(self, Pojistenec):
        params = (Pojistenec.jmeno, Pojistenec.prijmeni, Pojistenec.telefon, Pojistenec.vek)
        cur.execute(f'INSERT INTO pojistenci ("jmeno", "prijmeni", "telefon", "vek") VALUES (?, ?, ?, ?)', params)
        conn.commit()

    def vrat_pojistene(self):
        print("ID | Jmeno | Prijmeni | Tel. Cislo | Vek")
        print("========================================")
        for row in cur.execute('SELECT * FROM pojistenci'):
            x = 0
            for i in row:
                if x == 4:
                    print (i)
                    x = 0
                else:
                    print (i, end =" | ")
                    x += 1

    def vyhledej_pojisteneho(self):
        self.vyhledavani_jmeno = input("Zadejte jméno pojistného:\n")
        self.vyhledavani_prijmeni = input("Zadejte příjmení pojistného:\n")
        for row in cur.execute(f'SELECT * FROM pojistenci WHERE jmeno LIKE "%{self.vyhledavani_jmeno}%" '
                               f'AND prijmeni LIKE "%{self.vyhledavani_prijmeni}%";'):
            print (row)

