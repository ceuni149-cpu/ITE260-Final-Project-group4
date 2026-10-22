# NUMBER GUESSING GAME - ITE 260 Final Project
# Members: [Put names here]

import random

def generate_number():
    # Generates secret number from 1 to 100
    return random.randint(1, 100)

def check_guess(guess, secret):
    # Checks if guess is high, low, or correct
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    else:
        return "correct"

def play_game():
    # Main game logic
    secret = generate_number()
    tries = 0

    print("\n=== NUMBER GUESSING GAME ===")
    print("I picked a number from 1 to 100!")

    while True:
        try:
            guess = int(input("Your guess: "))
            tries += 1

            result = check_guess(guess, secret)

            if result == "high":
                print("Too high! Try lower.")
            elif result == "low":
                print("Too low! Try higher.")
            else:
                print(f"\nYou WIN! The number is {secret}")
                print(f"You guessed it in {tries} tries!")
                break
        except ValueError:
            print("Numbers only please!")

# Start the program
play_game()
