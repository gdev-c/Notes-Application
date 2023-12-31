"""
This is the only file that contains all the db calls

------------------------------------------------------------------------------------------
This module provides utility functions for all the CRUD operations on the DB
------------------------------------------------------------------------------------------

Author: Gowtham
Date: Dec 26, 2023
"""

import sqlite3

#------------------------------------------------------------------------------------------
#   Global variables
#------------------------------------------------------------------------------------------
create_user_details_query = """CREATE TABLE IF NOT EXISTS user_details
                            (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name varchar(255),
                            password_hash varchar(100),
                            password_salt varchar(20)
                            );
                            """

insert_into_user_details_table_query = """INSERT INTO user_details
                                    (name, password_hash, password_salt) 
                                    VALUES(?, ?, ?);"""

get_all_user_names_query = "SELECT user_details.name FROM user_details;"

get_user_password_query = "SELECT user_details.password_hash, user_details.password_salt FROM user_details WHERE user_details.name = ?;"

#------------------------------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------------------------------
def initialize_database():
    """
    This function initializes the database.
    Called only when the DB file is not present already
    Returns:
    True - Successful initialization of DB
    False - Unsuccessful initialization of DB
    """
    try:
        connection = sqlite3.connect('Notes.db')
        cur = connection.cursor()
        cur.execute(create_user_details_query)
        connection.commit()
    except sqlite3.Error as e:
        print('Error creating table.', e)
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()
    
    return True

def update_user_details_table(username, password_hash, salt):
    """
    Updates the user details table with user details entered
    """

    try:
        connection = sqlite3.connect('Notes.db')
        cur = connection.cursor()
        cur.execute(insert_into_user_details_table_query, (username, password_hash, salt))
        connection.commit()
    except sqlite3.Error as e:
        print('Error inserting to table.', e)
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()
    
    
    return True

def get_all_user_names():
    """
    Gets all the users available in the user_details table
    """
    rows = None
    try:
        connection = sqlite3.connect('Notes.db')
        cur = connection.cursor()
        cur.execute(get_all_user_names_query)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print('Error inserting to table.', e)
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()
    
    return rows

def get_password_for_user(user_name):
    """
    Get password hash and salt for a specific user
    """
    rows = None
    try:
        connection = sqlite3.connect('Notes.db')
        cur = connection.cursor()
        cur.execute(get_user_password_query, (user_name,))
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print('Error getting user deatils from table.', e)
    finally:
        if cur:
            cur.close()
        if connection:
            connection.close()

    if not rows: return ("", "")

    return (rows[0][0], rows[0][1])