import PySimpleGUI as sg
from components import layout as lay
from database import dbwrapper

sg.theme('Blue Purple')

def main():
    """
    Main entry point to the program.
    This gets the layout of all the windows and handles
    """
    
    layout = lay.main_page_layout()
    window = sg.Window('Welcome', layout, size=(800, 800), return_keyboard_events=True,  finalize=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close(); del window


if __name__ == '__main__':
    main()