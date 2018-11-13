import random

print 'DICE SIMULATOR'

# Number of dice
while True:
    try:
        num_dice = int(raw_input('How Many Dice: '))
        break
    except ValueError:
        print 'ERROR: Enter a Number.'

# Sides on die
while True:
    try:
        sides = int(raw_input('How Many Sides: '))
        break
    except ValueError:
        print 'ERROR: Enter a Number.'


def roll_die():
    # Roll die
    temp = random.randint(1, sides)
    return temp


print ''
while True:
    total = 0
    # Single Die
    if num_dice == 1:
        roll = roll_die()
        print 'Roll: ' + str(roll)
    # Two Dice
    elif num_dice == 2:
        roll1 = roll_die()
        roll2 = roll_die()
        total = roll1 + roll2
        print 'Die 1: ' + str(roll1)
        print 'Die 2: ' + str(roll2)
        print 'Sum: ' + str(total)
        # Check for doubles
        if roll1 == roll2:
            print 'DOUBLES!'
    # Multiple Dice
    else:
        for i in range(0, num_dice):
            roll = roll_die()
            # Record sum of rolls
            total += roll
            # Display each roll
            print 'Die ' + str(i + 1) + ': ' + str(roll)
        # Display sum
        print 'Sum: ' + str(total)

    # Prompt to continue rolling
    prompt = str(raw_input('Roll Again? (y/N): ')).upper()
    if prompt == 'Y' or prompt == '':
        print ''
        pass
    else:
        break
