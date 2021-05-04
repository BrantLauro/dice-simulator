from random import randint
import PySimpleGUI as sg

sg.theme('SandyBeach')

layout = [
    [sg.Text("What dice do you want to roll? [4/6/8/10/12/20/100]")],
    [sg.Input('', key='-INPUT-')],
    [sg.Output(key= '-OUTPUT-')],
    [sg.Button('Ok'), sg.Button('Quit')],
]

window = sg.Window("Dice Simulator", layout)

while True:
    events, values = window.Read()
    if events == sg.WINDOW_CLOSED or events == 'Quit':
        break
    dice_type = int(values['-INPUT-'])
    if dice_type in (4, 6, 8, 10, 12, 20, 100):
        dice = randint(1, dice_type)
        window['-OUTPUT-'].update('The value is: ' + str(dice))
