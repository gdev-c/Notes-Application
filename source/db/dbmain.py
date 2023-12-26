"""
This file is the entry point for all the DB calls. We call the use the DBWrapper objects only in this
file and not elsewhere for code readability.

------------------------------------------------------------------------------------------
This module provides utility functions for the DB class which is the main class used
for CRUD operations on the DB
------------------------------------------------------------------------------------------

Author: Gowtham
Date: Dec 26, 2023
"""

from dbwrapper import DB

def initialize_database():
    """
    This function initializes the database.
    Called only when the DB file is not present already
    """
    ret_val = False
    db_obj = DB()
    if db_obj.open_connection():
        query = """CREATE TABLE IF NOT EXISTS user_details
                            (user_id int PRIMARY KEY,
                            first_name varchar(255),
                            last_name varchar(255),
                            password_hash varchar(100),
                            password_salt varchar(20)
                            );
                            """
        if db_obj.execute_query(query):
            ret_val = True
        if db_obj.close_connection():
            print('Connection closed successfully.')
    return ret_val