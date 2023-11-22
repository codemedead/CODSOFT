import random
import time

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        print("Or Press 'e' to exit the game.")

        if user_choice in ['rock', 'paper', 'scissors', 'e']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user, computer):
    user = user.lower()  # Convert user choice to lowercase
    computer = computer.lower()  # Convert computer choice to lowercase

    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
            (user == 'scissors' and computer == 'paper') or \
            (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\n--- Rock, Paper, Scissors ---")

        user_choice = get_user_choice()
        if user_choice == 'e':
            print("Exiting the game.")
            print("Thanks for playing!")
            break
        computer_choice = get_computer_choice()
        print("Computer is choosing....")
        time.sleep(1)
        print(f"Computer chose: {computer_choice}")
        time.sleep(0.4)
        print(f"{user_choice} Vs. {computer_choice}")
        print(f"..................................................")
        time.sleep(1.5)
        result = determine_winner(user_choice, computer_choice)
        print("\n", result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1
        time.sleep(0.4)
        print(f"\n Your score: {user_score} | Computer's score: {computer_score}")

play_game()
