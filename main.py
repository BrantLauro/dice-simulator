from random import randint
choice = ' '
while True:
    while choice not in 'NY':
        choice = input('Do you want to roll a 6 face dice? [Y/N] ').upper().strip()[0]
        if choice == 'N':
            break
            choice = ' '
        if choice == 'Y':
            dice = randint(1, 6)
            print(dice)
            choice = ' '
