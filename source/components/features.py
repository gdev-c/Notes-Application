from db import dbmain
import os

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
        elif components == '-FILETABLE-':
            window[components].update([])
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

def create_directory_for_user(file_path):

    if not os.path.exists(file_path):
        os.makedirs(file_path)
        return True
    return False

def initialize_home_page(user_name):
    #Create directory for user if doesn't already exist
    file_path = os.path.join(os.getcwd(), 'files', user_name)
    if create_directory_for_user(file_path):
        return []
    
    return os.listdir(file_path)

def get_file_content(file_name, user_name):
    file_path = os.path.join(os.getcwd(), 'files', user_name, file_name)
    whole_content = ""
    with open(file_path, 'r') as file:
        whole_content += file.read()

    return whole_content

def write_content_to_file(content, user_name, file_name):
    file_path = os.path.join(os.getcwd(), 'files', user_name, file_name)
    with open(file_path, 'w') as file:
        file.write(content)
