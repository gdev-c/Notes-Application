import PySimpleGUI as sg
import os
from components import layout as lay, encrypt as en
#from database import dbmain

sg.theme('Blue Purple')

def main():
    """
    Main entry point to the program.
    This gets the layout of all the windows and handles
    """
    if os.path.exists(os.getcwd() + '/database/db.txt'):
        print('File found.\n')
        #dbmain.initialize_database()
    
    layout = lay.main_layout()
    # screen_width, screen_height = sg.Window.get_screen_size()
    # window_width = int(screen_width * 0.6)
    # window_height = int(screen_height * 0.6)
    window = sg.Window('Welcome', layout, finalize=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == None:
            break
        if event == '-SIGNIN-':
            # encrypt password
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