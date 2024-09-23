import random

# DRY -> Do not repeat yourself
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
associate = { ROCK: 'Rock', PAPER: 'Paper', SCISSORS: 'Scissors'}
choices = tuple(associate.keys())

def get_user_choice():
    while True:
        your_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if your_choice in choices:
            return your_choice
        else:
            print("Invalid choice!")

def display_choices(your_choice, computer_choice):
    print(f'You choose {associate[your_choice]}')
    print(f'Computer choose {associate[computer_choice]}')


def decider(your_choice, computer_choice):
    if your_choice == computer_choice:
        print('Tie!')
    elif (
        (your_choice == ROCK and computer_choice == SCISSORS) or
        (your_choice == SCISSORS and computer_choice == PAPER) or
        (your_choice == PAPER and computer_choice == ROCK)):
        print('You win!')
    else:
        print('You lose')

def play_game():
    while True:
        your_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(your_choice, computer_choice)

        decider(your_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()