# bazy danych - systemy do przechowywania danych
# baza sql w pythonie
import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect('baza.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
    """

    cursor.execute(query)
    sql_connection.commit()

    insert = """
    INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek','radek@radek.pl',10000);
    """
    # cursor.execute(insert)
    # sql_connection.commit()

    select = """
    SELECT * FROM developers;
    """

    for row in cursor.execute(select):
        print(row)  # (1, 'Radek', 'radek@radek.pl', 10000.0)

except sqlite3.Error as e:
    print('Błąd', e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
# Baza danych została podłączona
# Baza została zamknięta
