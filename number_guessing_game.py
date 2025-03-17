import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    attempts = 0
    while True:
        # Ask the user for their guess
        user_guess = int(input("Enter your guess: "))
        
        attempts += 1  # Count the number of attempts
        
        # Check if the user's guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the right number in {attempts} attempts.")
            break  # End the game when the user guesses correctly

# Call the function to start the game
number_guessing_game()
