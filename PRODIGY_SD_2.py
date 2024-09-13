import random

def guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
guessing_game()
