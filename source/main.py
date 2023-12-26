import PySimpleGUI as sg
import os
from components import layout as lay, encrypt as en, features
from db import dbmain

sg.theme('Blue Purple')

def main():
    """
    Main entry point to the program.
    This gets the layout of all the windows and handles
    """
    # if not os.path.exists(os.getcwd() + '\\Notes.db'):
    #     print('not exist.')
    #     dbmain.initialize_database()
    
    layout = lay.main_layout()
    window = sg.Window('Welcome', layout, finalize=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == None:
            break
        if event == '-SIGNIN-':
            #check if both fields are entered
            if values['-SIGNIN_USERNAME-'] == "" or values['-SIGNIN_PASSWORD-'] == "":
                sg.Popup('Enter all the fields to proceed')
                continue

            # check if user with same name already exists
            # if features.is_existing_user(values['-SIGNIN_USERNAME-']):
            #     sg.Popup('User with same name already exists. Please use a different name.')
            #     continue
            # encrypt password
            user_hash, user_salt = dbmain.get_password_for_user(values['-SIGNIN_USERNAME-'])
            hash_value, salt = en.encrypt_password(values['-SIGNIN_PASSWORD-'], user_salt)

            if hash_value == user_hash:
                sg.Popup('Passwords match')
            
            # read from DB and validate password

            # if correct password - go to next window/layout (home page)
            pass
        if event == '-SIGNUP-':
            # take to signup window
            #layout = lay.signup_page()
            #window = sg.Window('Welcome', layout, size=(window_width, window_height), finalize=True)
            window['-SIGNIN_LAYOUT-'].update(visible=False)
            window['-SIGNUP_LAYOUT-'].update(visible=True)
            pass
        if event == '-SIGNUP_NEW':
            # check for existing users with same name
            # write to DB
            # take to home page
            pass
        if event == '-SIGNUP_CANCEL-':
            # goes back to the welcome page
            #window = sg.Window('Welcome', layout, size=(window_width, window_height), finalize=True)
            window['-SIGNUP_LAYOUT-'].update(visible=False)
            window['-SIGNIN_LAYOUT-'].update(visible=True)
            pass

    window.close(); del window



if __name__ == '__main__':
    main()
    #os.remove('Notes.db')