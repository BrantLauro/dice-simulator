from random import randint
choice = ' '

print('''
 ____  _            ____  _                 _       _             
|  _ \(_) ___ ___  / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __ 
| | | | |/ __/ _ \ \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |_| | | (_|  __/  ___) | | | | | | | |_| | | (_| | || (_) | |   
|____/|_|\___\___| |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   
                                                                
''')

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
            
