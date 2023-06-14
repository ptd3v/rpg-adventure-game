import random
def roll_dice():
    return random.randint(1, 20)

print("Welcome to the 1d20 Dice Rolling Simulator!")
print("You roll a " + str(roll_dice()))

#The roll_dice() function uses the random.randint() function to generate a random number between 1 and 20, simulating the rolling of a 20-sided die (1d20).
#The main() function prompts the user to press Enter to roll the dice or 'q' to quit. If the user chooses to roll the dice, the program calls the roll_dice() function and displays the result.

import random

def roll_dice():
    return random.randint(1, 20)

def main():
    print("Welcome to the 1d20 Dice Rolling Simulator!")
    while True:
        user_input = input("Press enter to roll the dice or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        else:
            result = roll_dice()
            print("You rolled:", result)

if __name__ == '__main__':
    main()

#You can run this program, and each time you press Enter, it will generate a random number between 1 and 20, simulating the roll of a 20-sided die.