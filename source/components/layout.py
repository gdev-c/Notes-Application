import PySimpleGUI as sg

def main_layout():
    """
    Returns the layout of the sign-in and sign-up page
    """
    siginin_page_layout = [[sg.Text('NOTES', font=('Helvetica', 20))],
                            [sg.Text('Login', font=('Helvetica', 14))],
                            [sg.Text('User Name: ', font=('Helvetica', 14)), sg.Input(key='-SIGNIN_USERNAME-', enable_events=True)],
                            [sg.Text('Password:   ', font=('Helvetica', 14)), sg.Input(password_char='*', key='-SIGNIN_PASSWORD-')],
                            [sg.Button('Sign In', key='-SIGNIN-', font=('Helvetica', 12))],
                            [sg.Text('New?', text_color='blue', font=('Helvetica', 7)), sg.Button('Sign Up', key='-SIGNUP-', font=('Helvetica', 7), button_color=('blue', 'white'))]]
    
    signup_page_layout = [[sg.Text('Welcome to Notes', font=('Helvetica', 20))],
                            [sg.Text('User Name:            ', font=('Helvetica', 14)), sg.Input(key='-SIGNUP_USERNAME-')],
                            [sg.Text('Password:               ', font=('Helvetica', 14)), sg.Input(key='-SIGNUP_PASSWORD-')],
                            [sg.Text('Confirm Password:', font=('Helvetica', 14)), sg.Input(key='-SIGNUP_CONFIRM-')],
                            [sg.Button('Cancel', key='-SIGNUP_CANCEL-', font=('Helvetica', 7)), sg.Button('Sign Up:', key='-SIGNUP_NEW-', font=('Helvetica', 7))]]
    
    layout = [[sg.Column(siginin_page_layout, key='-SIGNIN_LAYOUT-'), sg.Column(signup_page_layout, key='-SIGNUP_LAYOUT-', visible=False)]]
    
    return layout