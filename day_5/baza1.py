# bazy danych - systemy do przechowywania danych
# baza sql w pythonie
import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect('baza.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print('Błąd', e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
# Baza danych została podłączona
# Baza została zamknięta
