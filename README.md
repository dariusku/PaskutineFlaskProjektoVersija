*****************************
Apie programą:
Programa sukurta, norint palengvinti restoranų klientų rezeracijos procedūrą, taip pat palengvinti restorano, bei jo darbuotojų darbą.
Klientas gali prisiregistruoti ir matyti restorano siūlomus produktus, laisvus staliukus, kuriuos galima rezervuoti.
Restoranas prisiregistravus gali pridėti savo siūlomus produktus, bei staliukus, kuriuos gali užsirezervuoti klientas.
*****************************
Programos paleidimas:

Atsidarius failą terminale paleidžiame šias komandas:

1. pip install -r requirements.txt (instaliuoti virtualią aplinką)
2. flask db init (atlikti duomenų bazės migracijas)
3. flask db migrate

Kitas žingsnis paleisti programą:
1. Paleisti main.py failą
2. Naršyklėje atidaryti puslapį http://127.0.0.1:7550/

Prisijungimai testui:

restorano prisijungimas:

test@test.lt   (email)
test  (slaptazodis)

kliento prisijungimas:



Numatomi programos patobulinimai:
1. Programa leidžia registruoti kelis restoranus, kuriuos gali pasirinkti klientai
2. Klientai , pamiršus slaptažodį gautų email pranešimą su slaptažodžio keitimo nuoroda.
