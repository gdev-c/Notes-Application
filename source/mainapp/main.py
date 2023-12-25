import PySimpleGUI as sg

sg.theme('Blue Purple')


def set_window_theme(themeName):
    """
    Sets the theme of the current window
    """
    sg.theme(themeName)


def get_welcome_page_layout():
    """
    Gets the layout of the main page
    """
    layout = [[sg.VPush()],
              [sg.Push(), sg.Text('NOTES', auto_size_text=True), sg.Push()],
              [sg.Push(), sg.Text('Login', auto_size_text=True), sg.Push()],
              [sg.Push(), sg.Text('User Name: '), sg.Input(key='-USERNAME-'), sg.Push()],
              [sg.Push(), sg.Text('Password:   '), sg.Input(key='-PASSWORD-', enable_events=True), sg.Push()],
              [sg.Push(), sg.Button('Sign In', key='SIGN_IN'), sg.Push()],
              [sg.VPush()]]

    return layout



def main():
    """
    Main entry point to the program.
    This gets the layout of all the windows and handles
    """
    sg.theme('Blue Purple')
    
    layout = get_welcome_page_layout()
    window = sg.Window('Welcome', layout, size=(800, 800), return_keyboard_events=True,  finalize=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close(); del window


if __name__ == '__main__':
    main()