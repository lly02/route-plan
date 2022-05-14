import sqlite3

def createTable(path):
    try:
        # DB creation
        con = sqlite3.connect(path)
    
        cur = con.cursor()

        # Table creation
        cur.execute('''
            CREATE TABLE bus_number(
                row_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bus_number INTERGER NOT NULL,
                bus_type TEXT NOT NULL
            );
        ''')

        con.close()

    except Exception as e:
        raise(e)
