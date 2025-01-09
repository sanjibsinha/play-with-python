import random
import os
import time
import math

def play_number_guessing_game():
    """
    A simple number guessing game.
    
    """

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = math.ceil(math.log2(100))  
    # Calculate maximum attempts using binary search

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    play_number_guessing_game()

'''
# Clear the screen (optional)
    if os.name == 'posix':  # For Unix/Linux/macOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')

    time.sleep(1)  # Pause for a moment

'''
    