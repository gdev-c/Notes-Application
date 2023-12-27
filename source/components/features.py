from db import dbmain

components_values = ['-SIGNIN_USERNAME-', '-SIGNIN_PASSWORD-', '-SIGNUP_PASSWORD-', '-SIGNUP_CONFIRM-',
                     '-SIGNUP_USERNAME-', '-SIGNUP_CHECKBOX-']

all_layouts = ['-SIGNIN_LAYOUT-', '-SIGNUP_LAYOUT-', '-TABLE_LAYOUT-']

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


def set_to_defaults(window):
    """
    Sets all the fields in all the windows to the default
    """
    for components in components_values:
        if components == '-SIGNUP_CHECKBOX-':
            window[components].update(False)
        else:
            window[components].update('')

    return window

def enable_layout(window, layout_str):
    for layout in all_layouts:
        if layout_str != layout:
            window[layout].update(visible=False)
        else:
            window[layout].update(visible=True)

    return window
