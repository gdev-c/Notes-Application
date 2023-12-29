from db import dbmain

#------------------------------------------------------------------------------------------
#   Global variables
#------------------------------------------------------------------------------------------
components_values = ['-SIGNIN_USERNAME-', '-SIGNIN_PASSWORD-', '-SIGNUP_PASSWORD-', '-SIGNUP_CONFIRM-',
                     '-SIGNUP_USERNAME-', '-SIGNUP_CHECKBOX-']

all_layouts = ['-SIGNIN_LAYOUT-', '-SIGNUP_LAYOUT-', '-TABLE_LAYOUT-']


#------------------------------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------------------------------
def is_existing_user(user_name):
    """
    Checks whether the user exists in our DB or not

    Returns:
    True: If user exists
    False: If no user exists with the given name in thr DB
    """
    rows = dbmain.get_all_user_names()
    if not rows: return False

    ret_val = False
    for row in rows:
        print(row[0], user_name)
        if row[0] == user_name:
            ret_val = True
            break

    return ret_val


def set_to_defaults(window):
    """
    Sets all the fields in all the windows to the default

    Returns:
    The window object
    """
    for components in components_values:
        if components == '-SIGNUP_CHECKBOX-':
            window[components].update(False)
        else:
            window[components].update('')

    return window

def enable_layout(window, layout_str):
    """
    Enables the layout that is given as argument and disables all the other layouts

    Returns:
    The window object
    """
    for layout in all_layouts:
        if layout_str != layout:
            window[layout].update(visible=False)
        else:
            window[layout].update(visible=True)

    return window

def get_current_user_notes(user_name):
    pass