import sqlite3

class DB:
    """
    This is a DB wrapper class for the sqlite3 database.
    Always use this class to read, write and update operations on the DB

    Attributes:
    - db_name: Name of the SQL Database
    - connection: Connection Object to the Database
    """

    def __init__(self, db_name="Notes.db"):
        self.db_name = db_name
        self.connection = None

    def open_connection(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error:
            print('Sqlite3 Error when connecting to DB.', sqlite3.Error)
            return False
        
        return True
    
    def execute_query(self, db_query=""):
        if not db_query: return False
        ret_val = True
        try:
            cur = self.connection.cursor()
            if cur:
                cur.execute(db_query)
                self.connection.commit()
                cur.close()
            else:
                print('Could Not get the cursor to the DB.\n')
        except sqlite3.Error:
            print('Sqlite3 Error when connecting to DB.', sqlite3.Error)
            ret_val =  False

        return ret_val
    
    def close_connection(self):
        if not self.connection: return False

        self.connection.close()
        return True

    def create_user_details_table(self):
        table_created = True
        try:
            connection = sqlite3.connect("")
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user_details
                            (user_id int PRIMARY KEY,
                            first_name varchar(255),
                            last_name varchar(255),
                            password_hash varchar(100),
                            password_salt varchar(20)
                            );
                            """)
            connection.commit()
        except sqlite3.Error:
            print('Sqlite error.\n')
            table_created = False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
        return table_created
    
    def create_note_table(self):
        table_created = True
        try:
            connection = sqlite3.connect("")
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS notes_metadata
                           (note_id int PRIMARY_KEY,
                           file_path varchar(255),
                           last_modifed_at date,
                           FOREIGN KEY (user_id) REFERENCES user_details(user_id)
                           );
                           """)
            connection.commit()
        except:
            print('Sqlite Error.\n')
            table_created = False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        
        return table_created