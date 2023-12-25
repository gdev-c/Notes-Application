import PySimpleGUI as sg

def main_page_layout():
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