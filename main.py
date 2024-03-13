from art import logo
import random
import os

#clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

# Function to check if the guess is correct
def check_guess(guess, answer):
    if guess == answer:
        return True
    return False

# Function to compare the guess with the answer
def compare_guess(guess, answer):
    if guess == answer:
        print(f"🎉 You got it! The answer is {answer} :D")
    else:
        if guess < answer:
            print("Too low")
        else:
            print("Too high")
        print("Guess again. 😊")

    return

# Function to play the game
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    # Computer picks a number between 1 and 100
    comp_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100 :) I'll let you guess")

    # User chooses a difficulty level
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    # User gets a certain number of attempts based on the difficulty level
    attempt = 5 if level == "hard" else 10
    # User guesses a number
    while attempt:
        # Let user know how many attempts they have remaining
        print(f"You have {attempt}(s) remaining to guess a number.")
        guess = int(input("Make a guess: "))
        # Check if the guess is correct
        if check_guess(guess, comp_number):
            # If the guess is correct, let the user know and end the game
            compare_guess(guess, comp_number)
            break
        # If the guess is incorrect, let the user know and continue the game
        compare_guess(guess, comp_number)
        attempt -= 1

    if not attempt:  
        print(f"The number was {comp_number}. Better luck next time! 😊")

    return

# Main function
def main():
    play_game()
    while input("Do you want to play again? Type 'yes' or 'no': ") == "yes":
        clear()
        play_game()
    print("Goodbye! 😊")

    return

# Run the main function
if __name__ == "__main__":
    main()


