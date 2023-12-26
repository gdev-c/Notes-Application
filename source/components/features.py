from db import dbmain

def is_existing_user(user_name):
    rows = dbmain.get_all_user_names()
    if not rows: return False

    ret_val = False
    for row in rows:
        print(row[0], user_name)
        if row[0] == user_name:
            ret_val = True
            break

    return ret_val