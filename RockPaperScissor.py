import random

# DRY -> Do not repeat yourself
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
associate = { ROCK: 'Rock', PAPER: 'Paper', SCISSORS: 'Scissors'}
choices = tuple(associate.keys())

def get_user_choice():
    while True:
        response = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if response in choices:
            return response
        else:
            print("Invalid choice!")

def display_choices(response, computer_choice):
    print(f'You choose {associate[response]}')
    print(f'Computer choose {associate[computer_choice]}')


def decider(response, computer_choice):
    if response == computer_choice:
        print('Tie!')
    elif (
        (response == ROCK and computer_choice == SCISSORS) or
        (response == SCISSORS and computer_choice == PAPER) or
        (response == PAPER and computer_choice == ROCK)):
        print('You win!')
    else:
        print('You lose')

def play_game():
    while True:
        response = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(response, computer_choice)

        decider(response, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()