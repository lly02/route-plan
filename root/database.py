from socket import create_connection
import sqlite3

class db:
    def __init__(self, path, db_name):
        self.path = path
        self.db_name = db_name

    def create_connection(self):
        try:
            return sqlite3.connect(self.path)

        except Exception as e:
            raise(e)

    def close_connection(self, con):
        try:
            return con.close()
        
        except Exception as e:
            raise(e)


    def create_table(self):
        con = self.create_connection()
        cur = con.cursor()

        query = '''
            CREATE TABLE bus(
                row_id INTEGER PRIMARY KEY AUTOINCREMENT,
                bus_number TEXT NOT NULL,
                bus_type TEXT NOT NULL
            );
        '''

        try:
            # Table creation
            cur.execute(query)

        except Exception as e:
            raise(e)

        self.close_connection(con)

    def insert_data(self, data):
        con = self.create_connection()
        cur = con.cursor()

        query = '''
            INSERT INTO bus
                (bus_number, bus_type)
            VALUES 
                (?, ?)
        '''
        query_params = []

        for key, values in data.items():
            for item in values:
                query_params.append((item, key))

        try:
            cur.executemany(query, query_params)
            con.commit()

        except Exception as e:
            raise(e)
            
        self.close_connection(con)
