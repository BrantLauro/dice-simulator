from random import randint
import PySimpleGUI as sg

layout = [
    [sg.Text('Dice Simulator')]
    [sg.Input('Do you want to roll a dice? [Y/N]', key='choice')]
    [sg.Button('Enter')]
]
self.window = sg.Window("Dice Simulator").layout(layout)
self.button, self.values = window.Read()

def start(self):
    print(self.values)

ui = dice_simulator()
ui.start()

choice = ' '
while True:
    while choice not in 'NY':
        choice = input('Do you want to roll a dice? [Y/N] ').upper().strip()[0]
        if choice == 'N':
            break
            choice = ' '
        if choice == 'Y':
            choice_dice = 0
            while choice_dice not in (4, 6, 8, 10, 12, 20, 100): 
                choice_dice = int(input('What dice do you want to roll? [4/6/8/10/12/20/100] '))
            dice = randint(1, choice_dice)
            print(dice)
            dice = 0
            choice_dice = ' '
            choice = ' '
