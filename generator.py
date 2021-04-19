import cx_Oracle
import names
import random
from pesel import Pesel

user = "login"
password = "password"

tables = {
    1: "Kurs",
    2: "Nauczyciel",
    3: "Znane_jezyki",
    4: "Jezyk",
    5: "Tematyka",
    6: "Poziom",
    7: "Uczestnicy_kursu",
    8: "Uczen",
    9: "Test_wstepny",
    10: "Wplata",
    11: "Wszystkie tabele"
}

for key_tables, value_tables in tables.items():
    print(f'{key_tables}: {value_tables}')

print()


while True:
    try:
        chosen_table = int(input("Wybierz tabele:"))
        if chosen_table < 1 or chosen_table > 11:
            print("Musisz podać liczbe od 1 do 11")
        else:
            break
    except ValueError:
        print("Musisz podać liczbe")

print()
print(tables[chosen_table])
print()

while True:
    try:
        rows = int(input("Ile wierszy:"))
        break
    except ValueError:
        print("Musisz podać cyfre!")

# JEZYK
id_jezyk = []
nazwa_jezyka = []

for i in range(1, rows+1):
    x = str(i)
    id_jezyk.append(x)
    nazwa_jezyka.append('jezyk'+x)

query_jezyk = list(zip(
    id_jezyk,
    nazwa_jezyka))

# TEMATYKA
id_tematyka = []
nazwa_tematyki = []

for i in range(1,rows+1):
    x = str(i)
    id_tematyka.append(x)
    nazwa_tematyki.append('tematyka'+x)

query_tematyka = list(zip(
    id_tematyka,
    nazwa_tematyki))

# NAUCZYCIEL
id_nauczyciel = []
imie_nauczyciel = []
nazwisko_nauczyciel = []
data_urodzenia_nauczyciel = []
pesel_nauczyciel = []
email_nauczyciel = []
nr_tel_nauczyciel = []

for i in range(1, rows + 1):
    x = str(i)
    id_nauczyciel.append(x)
    imie_nauczyciel.append(names.get_first_name())
    nazwisko_nauczyciel.append(names.get_last_name())
    pesel = str(Pesel.generate())
    data_urodzenia_nauczyciel.append(pesel[0:-9]+ "/" + pesel[2:-7] + "/" + pesel[4:-5])
    pesel_nauczyciel.append(pesel)
    email_nauczyciel.append(imie_nauczyciel[i-1] + "." + nazwisko_nauczyciel[i-1] + "@poliglota.pl")
    nr_tel_nauczyciel.append(random.randint(100000000,999999999))

query_nauczyciel = list(zip(
    id_nauczyciel,
    imie_nauczyciel,
    nazwisko_nauczyciel,
    data_urodzenia_nauczyciel,
    pesel_nauczyciel,
    email_nauczyciel,
    nr_tel_nauczyciel))

# UCZEN
id_uczen = []
imie_uczen = []
nazwisko_uczen = []
data_urodzenia_uczen = [] 
pesel_uczen = []
email_uczen = []
nr_tel_uczen = []

for i in range(1, rows+1):
    x = str(i)
    id_uczen.append(x)
    imie_uczen.append(names.get_first_name())
    nazwisko_uczen.append(names.get_last_name())
    pesel = str(Pesel.generate())
    data_urodzenia_uczen.append(pesel[0:-9]+ "/" + pesel[2:-7] + "/" + pesel[4:-5])
    pesel_uczen.append(pesel)
    email_uczen.append(imie_uczen[i-1] + "." + nazwisko_uczen[i-1] + "@uczen.poliglota.pl")
    nr_tel_uczen.append(random.randint(100000000,999999999))

query_uczen = list(zip(
    id_uczen,
    imie_uczen,
    nazwisko_uczen,
    data_urodzenia_uczen,
    pesel_uczen,
    email_uczen,
    nr_tel_uczen))

# POZIOM
id_poziom = []
nazwa_poziomu = []

for i in range(1,rows+1):
    x = str(i)
    id_poziom.append(x)
    nazwa_poziomu.append('poziom'+x)

query_poziom = list(zip(
    id_poziom,
    nazwa_poziomu))

# ZNANE_JEZYKI
id_znane_jezyki = []
znane_jezyki = []

for i in range(1,rows+1):
    x = str(i)
    id_znane_jezyki.append(x)
    id_nauczyciel.append(x)
    znane_jezyki.append('jezyk'+x)

query_znane_jezyki = list(zip(
    id_znane_jezyki,
    id_nauczyciel,
    znane_jezyki
))
# KURS
id_kurs = []
data_rozpoczecia_kurs = []
data_zakonczenia_kurs = []
liczba_godzin_kurs = []
cena_kurs = []
            
for i in range(1, rows+1):
    x = str(i)
    id_kurs.append(x)
    id_tematyka.append(x)
    id_jezyk.append(x)
    id_poziom.append(x)
    id_nauczyciel.append(x)
    year = random.randint(2010,2021)
    month = random.randint(1,12)
    month_diff = random.randint(1,3)
    if (month + month_diff) > 12:
        year_end = year + 1
        month_end = month + month_diff - 12
    else:
        month_end = month + month_diff
        year_end = year
    day = random.randint(1,28)
    data_rozpoczecia_kurs.append(str(year) + '/' + str(month) + "/" + str(day))
    data_zakonczenia_kurs.append(str(year_end) + '/' + str(month_end) + "/" + str(day))
    liczba_godzin_kurs.append(random.randint(5,40))
    cena_kurs.append(random.randint(50,250))

query_kurs = list(zip(
    id_kurs,
    id_tematyka,
    id_jezyk,
    id_poziom,
    id_nauczyciel,
    data_rozpoczecia_kurs,
    data_zakonczenia_kurs,
    liczba_godzin_kurs,
    cena_kurs
))

# UCZESTNICY_KURSU
id_uczestnicy = []

for i in range(1, rows+1):
    x = str(i)
    id_uczestnicy.append(x)
    id_uczen.append(x)
    id_kurs.append(x)

query_uczestnicy_kursu = list(zip(
    id_uczestnicy,
    id_uczen,
    id_kurs
))

# TEST_WSTEPNY
id_test = []
wynik = []
zalacznik = []

for i in range(1, rows+1):
    x = str(i)
    id_test.append(x)
    id_uczen.append(x)
    wynik.append(random.randint(1,100))
    zalacznik.append('zalacznik'+x)

query_test_wstepny = list(zip(
    id_test,
    id_uczen,
    wynik,
    zalacznik
))

#WPLATA
id_wplata = []
data_wplata = []
kwota_wplata = []
potwierdzenie_zalacznik_wplata = []


for i in range(1, rows+1):
    x = str(i)
    id_wplata.append(x)
    id_uczen.append(x)
    year_wplata = random.randint(2010,2021)
    month_wplata = random.randint(1,12)
    day_wplata = random.randint(1,28)
    data_wplata.append(str(year_wplata) + '/' + str(month_wplata) + "/" + str(day_wplata))
    kwota_wplata.append(random.randint(50,250))
    potwierdzenie_zalacznik_wplata.append('zalacznik'+x)

query_wplata = list(zip(
    id_wplata,
    id_uczen,
    data_wplata,
    kwota_wplata,
    potwierdzenie_zalacznik_wplata
))

try:
    connection = cx_Oracle.connect(user, password, 'myservice')
except Exception as err:
    print('Error while creating the connection', err)
else:
    try:
        cursor = connection.cursor()
    except Exception as err:
        print('Error while inserting the data ', err)
    else:
        sql_delete = """ DELETE FROM ZNANE_JEZYKI """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM UCZESTNICY_KURSU """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM UCZEN """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM KURS """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM JEZYK """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM TEMATYKA """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM NAUCZYCIEL """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM POZIOM """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM TEST_WSTEPNY """
        cursor.execute(sql_delete)
        sql_delete = """ DELETE FROM WPLATA """
        cursor.execute(sql_delete)

        f = open("inserts.txt", "a")

        if chosen_table == 1: # Kurs
            sql_insert = """ INSERT INTO TEMATYKA VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_tematyka)
            for i in range(1, rows + 1):
                f.write("INSERT INTO TEMATYKA VALUES " + str(query_tematyka[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO JEZYK VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_jezyk)
            for i in range(1, rows + 1):
                f.write("INSERT INTO JEZYK VALUES " + str(query_jezyk[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO POZIOM VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_poziom)
            for i in range(1, rows + 1):
                f.write("INSERT INTO POZIOM VALUES " + str(query_poziom[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO NAUCZYCIEL VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_nauczyciel)
            for i in range(1, rows + 1):
                f.write("INSERT INTO NAUCZYCIEL VALUES " + str(query_nauczyciel[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO KURS VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"""
            cursor.executemany(sql_insert, query_kurs)
            for i in range(1, rows + 1):
                f.write("INSERT INTO KURS VALUES " + str(query_kurs[i-1])+";")
                f.write('\n')

        elif chosen_table == 2:  # Nauczyciel

            sql_insert = """ INSERT INTO NAUCZYCIEL VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_nauczyciel)
            for i in range(1, rows + 1):
                f.write("INSERT INTO NAUCZYCIEL VALUES " + str(query_nauczyciel[i-1])+";")
                f.write('\n')

        elif chosen_table == 3:  # Znane_jezyki

            sql_insert = """ INSERT INTO NAUCZYCIEL VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_nauczyciel)
            for i in range(1, rows + 1):
                f.write("INSERT INTO NAUCZYCIEL VALUES " + str(query_nauczyciel[i-1])+";")
                f.write('\n')           
            sql_insert = """ INSERT INTO ZNANE_JEZYKI VALUES (:1, :2, :3) """
            cursor.executemany(sql_insert, query_znane_jezyki)
            for i in range(1, rows + 1):
                f.write("INSERT INTO ZNANE_JEZYKI VALUES " + str(query_znane_jezyki[i-1])+";")
                f.write('\n')

        elif chosen_table == 4:  # Jezyk
            
            sql_insert = """ INSERT INTO JEZYK VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_jezyk)
            for i in range(1, rows + 1):
                f.write("INSERT INTO JEZYK VALUES " + str(query_jezyk[i-1])+";")
                f.write('\n')

        elif chosen_table == 5:  # Tematyka

            sql_insert = """ INSERT INTO TEMATYKA VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_tematyka)
            for i in range(1, rows + 1):
                f.write("INSERT INTO TEMATYKA VALUES " + str(query_tematyka[i-1])+";")
                f.write('\n')

        elif chosen_table == 6:  # Poziom

            sql_insert = """ INSERT INTO POZIOM VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_poziom)
            for i in range(1, rows + 1):
                f.write("INSERT INTO POZIOM VALUES " + str(query_poziom[i-1])+";")
                f.write('\n')
                
        elif chosen_table == 7:  # Uczestnicy_kursu

            sql_insert = """ INSERT INTO UCZEN VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_uczen)
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZEN VALUES " + str(query_uczen[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO TEMATYKA VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_tematyka)
            for i in range(1, rows + 1):
                f.write("INSERT INTO TEMATYKA VALUES " + str(query_tematyka[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO JEZYK VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_jezyk)
            for i in range(1, rows + 1):
                f.write("INSERT INTO JEZYK VALUES " + str(query_jezyk[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO POZIOM VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_poziom)
            for i in range(1, rows + 1):
                f.write("INSERT INTO POZIOM VALUES " + str(query_poziom[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO NAUCZYCIEL VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_nauczyciel)
            for i in range(1, rows + 1):
                f.write("INSERT INTO NAUCZYCIEL VALUES " + str(query_nauczyciel[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO KURS VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"""
            cursor.executemany(sql_insert, query_kurs)
            for i in range(1, rows + 1):
                f.write("INSERT INTO KURS VALUES " + str(query_kurs[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO UCZESTNICY_KURSU VALUES (:1, :2, :3) """
            cursor.executemany(sql_insert, query_uczestnicy_kursu)
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZESTNICY_KURSU VALUES " + str(query_uczestnicy_kursu[i-1])+";")
                f.write('\n')
            
        elif chosen_table == 8:  # Uczen 
            
            sql_insert = """ INSERT INTO UCZEN VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_uczen)            
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZEN VALUES " + str(query_uczen[i-1])+";")
                f.write('\n')

        elif chosen_table == 9:  # Test_wstepny

            sql_insert = """ INSERT INTO UCZEN VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_uczen)
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZEN VALUES " + str(query_uczen[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO TEST_WSTEPNY VALUES (:1, :2, :3, :4) """
            cursor.executemany(sql_insert, query_test_wstepny)
            for i in range(1, rows + 1):
                f.write("INSERT INTO TEST_WSTEPNY VALUES " + str(query_test_wstepny[i-1])+";")
                f.write('\n')

        elif chosen_table == 10: # Wplata

            sql_insert = """ INSERT INTO UCZEN VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_uczen)
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZEN VALUES " + str(query_uczen[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO WPLATA VALUES (:1, :2, :3, :4, :5) """
            cursor.executemany(sql_insert, query_wplata)
            for i in range(1, rows + 1):
                f.write("INSERT INTO WPLATA VALUES " + str(query_wplata[i-1])+";")
                f.write('\n')

        elif chosen_table == 11: # Wszystkie tabele
            sql_insert = """ INSERT INTO JEZYK VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_jezyk)
            for i in range(1, rows + 1):
                f.write("INSERT INTO JEZYK VALUES " + str(query_jezyk[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO TEMATYKA VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_tematyka)
            for i in range(1, rows + 1):
                f.write("INSERT INTO TEMATYKA VALUES " + str(query_tematyka[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO NAUCZYCIEL VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_nauczyciel)
            for i in range(1, rows + 1):
                f.write("INSERT INTO NAUCZYCIEL VALUES " + str(query_nauczyciel[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO UCZEN VALUES (:1, :2, :3, :4, :5, :6, :7) """
            cursor.executemany(sql_insert, query_uczen)
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZEN VALUES " + str(query_uczen[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO POZIOM VALUES (:1, :2) """
            cursor.executemany(sql_insert, query_poziom)
            for i in range(1, rows + 1):
                f.write("INSERT INTO POZIOM VALUES " + str(query_poziom[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO ZNANE_JEZYKI VALUES (:1, :2, :3) """
            cursor.executemany(sql_insert, query_znane_jezyki)
            for i in range(1, rows + 1):
                f.write("INSERT INTO ZNANE_JEZYKI VALUES " + str(query_znane_jezyki[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO KURS VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)"""
            cursor.executemany(sql_insert, query_kurs)
            for i in range(1, rows + 1):
                f.write("INSERT INTO KURS VALUES " + str(query_kurs[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO UCZESTNICY_KURSU VALUES (:1, :2, :3) """
            cursor.executemany(sql_insert, query_uczestnicy_kursu)
            for i in range(1, rows + 1):
                f.write("INSERT INTO UCZESTNICY_KURSU VALUES " + str(query_uczestnicy_kursu[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO TEST_WSTEPNY VALUES (:1, :2, :3, :4) """
            cursor.executemany(sql_insert, query_test_wstepny)
            for i in range(1, rows + 1):
                f.write("INSERT INTO TEST_WSTEPNY VALUES " + str(query_test_wstepny[i-1])+";")
                f.write('\n')
            sql_insert = """ INSERT INTO WPLATA VALUES (:1, :2, :3, :4, :5) """
            cursor.executemany(sql_insert, query_wplata)
            for i in range(1, rows + 1):
                f.write("INSERT INTO WPLATA VALUES " + str(query_wplata[i-1])+";")
                f.write('\n')

        print('Insert completed')
        connection.commit()
finally:
    cursor.close()
    connection.close()

f.close()