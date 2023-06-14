import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 0 

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", attempts)
        break
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

guess_number()