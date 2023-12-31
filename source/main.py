import PySimpleGUI as sg
import os
from components import layout as lay, encrypt as en, features
from db import dbmain

#------------------------------------------------------------------------------------------
#   Global Variables
#------------------------------------------------------------------------------------------
current_user = None
file_list = []

#------------------------------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------------------------------
def event_loop(window):
    """
    This is the event loop for the windows in the notes app
    """
    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WIN_CLOSED or event == None:
            break

        elif event == '-SIGNIN-':
            #check if both fields are entered
            if values['-SIGNIN_USERNAME-'] == "" or values['-SIGNIN_PASSWORD-'] == "":
                sg.Popup('Enter all the fields to proceed')
                continue

            # encrypt password
            # read from DB and validate password
            user_hash, user_salt = dbmain.get_password_for_user(values['-SIGNIN_USERNAME-'])
            if user_hash == "" or user_salt == "":
                sg.Popup('No user with the name exists. Please verify the username or Create a New account.')
                continue
            hash_value, salt = en.encrypt_password(values['-SIGNIN_PASSWORD-'], user_salt)
            
            # if correct password - go to next window/layout (home page)
            if hash_value == user_hash:
                window = features.set_to_defaults(window)
                window = features.enable_layout(window, '-TABLE_LAYOUT-')
            
            current_user = values['-SIGNIN_USERNAME-']
            file_list = features.initialize_home_page(current_user)
            if len(file_list) != 0:
                window['-FILETABLE-'].update(values=file_list)
            
        elif event == '-SIGNUP-':
            # take to signup window
            window = features.set_to_defaults(window)
            window = features.enable_layout(window, '-SIGNUP_LAYOUT-')
            
        elif event == '-SIGNUP_NEW-':
            if values['-SIGNUP_USERNAME-'] == "" or values['-SIGNUP_PASSWORD-'] == "" or values['-SIGNUP_CONFIRM-'] == "":
                sg.Popup('Enter all the fields to proceed')
                continue

            if values['-SIGNUP_PASSWORD-'] != values['-SIGNUP_CONFIRM-']:
                sg.Popup("Passwords don't match.")
                continue
             
            # check for existing users with same name
            if features.is_existing_user(values['-SIGNIN_USERNAME-']):
                sg.Popup('User with same name already exists. Please use a different name.')
                continue

            # write to DB
            password_hash, password_salt = en.encrypt_password(values['-SIGNUP_PASSWORD-'])
            dbmain.update_user_details_table(values['-SIGNUP_USERNAME-'], password_hash, password_salt)

            current_user = values['-SIGNUP_USERNAME-']
            # take to home page
            features.enable_layout(window, '-TABLE_LAYOUT-')

        elif event == '-SIGNUP_CANCEL-':
            # goes back to the welcome page
            window = features.enable_layout(window, '-SIGNIN_LAYOUT-')
            window = features.set_to_defaults(window)

        elif event == '-SIGNUP_CHECKBOX-':
            window['-SIGNUP_PASSWORD-'].update(password_char='' if values['-SIGNUP_CHECKBOX-'] else '*')
            window['-SIGNUP_CONFIRM-'].update(password_char='' if values['-SIGNUP_CHECKBOX-'] else '*')

        elif event == '-FILETABLE-':
            if values['-FILETABLE-'][0] >= len(file_list): return
            file_name = file_list[values['-FILETABLE-'][0]]
            content = features.get_file_content(file_name, current_user)
            window['-NOTE_AREA-'].update(content)

        elif event == '-SAVE_NOTE-':
            if values['-FILETABLE-'][0] >= len(file_list): return
            file_name = file_list[values['-FILETABLE-'][0]]
            features.write_content_to_file(values['-NOTE_AREA-'], current_user, file_name)

        elif event == '-EXIT_NOTE-':
            current_user = None
            file_list = []
            window = features.enable_layout(window, '-SIGNIN_LAYOUT-')
            window = features.set_to_defaults(window)

        elif event == 'New':
            #file_path = os.path.join(os.getced(), 'files', current_user, )
            sg.popup('Make sure to create a new file in your directory.')
            file_path = sg.popup_get_file('Save As', save_as=True, file_types=(("Text Files", "*.txt"), ("All Files", "*.*")))
            if file_path:
                with open(file_path, 'w') as new_file:
                    new_file.write('')
            file_list = features.initialize_home_page(current_user)
            if len(file_list) != 0:
                window['-FILETABLE-'].update(values=file_list)

        elif event == 'Delete':
            confirmation = sg.PopupYesNo('Are you sure you want to delete this file?')
            if not confirmation: continue
            if values['-FILETABLE-'][0] >= len(file_list): return
            file_name = file_list[values['-FILETABLE-'][0]]
            file_path = os.path.join(os.getcwd(), 'files', current_user, file_name)
            os.remove(file_path)
            file_list = features.initialize_home_page(current_user)
            if len(file_list) != 0:
                window['-FILETABLE-'].update(values=file_list)

def main():
    """
    Main entry point to the program.
    This gets the layout of all the windows and handles
    """
    if not os.path.exists(os.getcwd() + '\\Notes.db'):
        dbmain.initialize_database()
    
    layout = lay.main_layout()
    window = sg.Window('Welcome', layout, finalize=True)

    event_loop(window)
    
    window.close(); del window


#This is the entry point of the application
if __name__ == '__main__':
    main()
    #os.remove('Notes.db')